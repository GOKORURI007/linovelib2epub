import logging
import os
import sys
import traceback
from logging import (CRITICAL, DEBUG, ERROR, INFO, WARN, WARNING, FileHandler, StreamHandler,Formatter, getLogger)
from os import path
from time import localtime, strftime
from typing import Optional

from rich.logging import RichHandler

DEFAULT_LOG_FOLDER = os.path.join(os.path.dirname(os.getcwd()), 'logs')

class Logger:
    LEVEL_MAP = {
        'INFO': INFO,
        'DEBUG': DEBUG,
        'WARN': WARN,
        'WARNING': WARNING,
        'ERROR': ERROR,
        'CRITICAL': CRITICAL,
    }

    def __init__(self,
                 logger_level: Optional[str] = "INFO",
                 logger_name: Optional[str] = "logger",
                 log_dir: Optional[str] = None,
                 log_filename: Optional[str] = None):
        self.logger = None
        self.level = self.LEVEL_MAP.get(logger_level, 'INFO')
        self.name = logger_name
        self.log_dir = log_dir or DEFAULT_LOG_FOLDER
        self.log_filename = log_filename or strftime("%Y-%m-%d", localtime())
        self._set_logger()

    def _set_logger(self):
        try:
            os.makedirs(self.log_dir)
        except (FileExistsError, OSError):
            pass

        self.logger = getLogger(self.name)

        # HANDLERS
        # If stream is not specified, sys.stderr is used.
        # If you need sys.stdout, pass it to StreamHandler constructor()
        # stream_handler = StreamHandler()
        shell_handler = RichHandler(rich_tracebacks=True)

        file_handler = FileHandler(
            filename=os.path.join(self.log_dir, f"{self.log_filename}.log"),
            mode="a",
            encoding="utf-8",
        )

        # LOG LEVELS
        self.logger.setLevel(self.level)
        shell_handler.setLevel(self.level)
        file_handler.setLevel(self.level)

        # LOG FORMAT
        fmt_shell = '%(name)s %(message)s'
        fmt_file = '%(asctime)s %(levelname)-8s %(name)-20s %(filename)-15s:%(lineno)-5d %(message)s'
        datefmt = '%Y-%m-%d,%H:%M:%S'

        # LOG FORMATTER
        # 2023-02-02,13:07:55 INFO     [logger2] Logging set up.             logger2.py:30
        # Warning: rich will add some logging formats to fmt_shell
        shell_formatter = Formatter(fmt_shell, datefmt)
        # [2023-02-02,13:07:55][ERROR][logger2][logger2.py:division:37] Oh noes!
        file_formatter = Formatter(fmt_file, datefmt)

        shell_handler.setFormatter(shell_formatter)
        file_handler.setFormatter(file_formatter)

        self.logger.handlers.clear()
        self.logger.addHandler(shell_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


class MultiprocessingLogHelper:

    def __init__(self, queue, log_name, log_file_path = None):
        self.queue = queue
        self.log_name = log_name
        self.log_file_path = log_file_path or DEFAULT_LOG_FOLDER
        self.logger = self.listener_configurer()

    def listener_configurer(self):
        """ Configures and returns a log file based on
        the given name

        Arguments:
            log_name (str): String of the log name to use
            log_file_path (str): String of the log file path

        Returns:
            logger: configured logging object
        """
        logger = logging.getLogger(self.log_name)

        # fh = logging.FileHandler(
        #     path.join(self.log_file_path, f'{self.log_name}.log'), encoding='utf-8')
        # fmtr = logging.Formatter(
        #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fh.setFormatter(fmtr)
        logger.setLevel(logging.INFO)

        # current_fh_names = [fh.__dict__.get(
        #     'baseFilename', '') for fh in logger.handlers]
        # if not fh.__dict__['baseFilename'] in current_fh_names:  # This prevents multiple logs to the same file
        #     logger.addHandler(fh)

        stream_hanlder = StreamHandler()
        # logger.addHandler(fh)
        logger.addHandler(stream_hanlder)

        return logger

    def listener_process(self):
        """ Listener process is a target for a multiprocess process
        that runs and listens to a queue for logging events.

        Arguments:
            queue (multiprocessing.manager.Queue): queue to monitor
            configurer (func): configures loggers
            log_name (str): name of the log to use

        Returns:
            None
        """
        self.listener_configurer()

        while True:
            try:
                record = self.queue.get()
                if record is None:
                    break
                print(f'record: {record}')
                logger = logging.getLogger(record.name)
                logger.handle(record)
            except Exception:
                print('Failure in listener_process', file=sys.stderr)
                traceback.print_last(limit=1, file=sys.stderr)
