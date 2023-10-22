```diff
+ 🚀 真白萌小说站 https://masiro.me 已经得到支持 🚀
+ 🚩 轻小说文库 https://www.wenku8.net/login.php 已经得到支持 🚩
```

# linovelib2epub

Crawl light novel from [哔哩轻小说 (linovelib)](https://w.linovelib.com/) and convert to epub.

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg?style=flat)](https://github.com/pypa/hatch)
[![flake8](https://img.shields.io/badge/linter-flake8-brightgreen)](https://github.com/PyCQA/flake8)
[![Build and Publish](https://github.com/lightnovel-center/linovelib2epub/actions/workflows/build-and-publish.yml/badge.svg?branch=main)](https://github.com/lightnovel-center/linovelib2epub/actions/workflows/build-and-publish.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/linovelib2epub?color=blue&label=PyPI%20Download)
![PyPI](https://img.shields.io/pypi/v/linovelib2epub)
![Lines of code](https://www.aschey.tech/tokei/github/lightnovel-center/linovelib2epub)
[![Hits-of-Code](https://hitsofcode.com/github/lightnovel-center/linovelib2epub?branch=main)](https://hitsofcode.com/github/lightnovel-center/linovelib2epub/view?branch=main)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/lightnovel-center/linovelib2epub)

## preview

> A picture is worth a thousand words. Talk is cheap, show me the real effect.

![preview](./preview.gif)

> This demo use [this screen recorder tool](https://github.com/faressoft/terminalizer) to record.

## Features

- [x] flexible `has_illustration` and `divide_volume` option for epub output
- [x] support downloading a certain volume of a novel
- [x] built-in http request retry mechanism to improve network fault tolerance
- [x] built-in random browser user_agent through fake_useragent library
- [x] built-in strict integrity check about image download
- [x] built-in mechanism for saving temporary book data by pickle library
- [x] use asyncio/multiprocessing to download images
- [x] support adding custom css styles to epub

## Supported  Websites (plan)

| 序号  | 网站名称                                         | 语言    | 爬虫难度 | 支持进度                                | 备注                           | 技术难点                                        |
|-----|----------------------------------------------|-------|------|-------------------------------------|------------------------------|---------------------------------------------|
| 1   | [哔哩轻小说（Mobile）](https://w.linovelib.com/)    | 简 / 繁 | 中😰  | <img src="./merrli.png" width="36"> | ` 不用登录 ` ` 一章多页 `            | `JS 加密` `JS文件随机` ` 章节链接破损 ` `Cloudflare 保护 ` |
| 2   | ~~[哔哩轻小说（Web）](https://www.linovelib.com/)~~ | 简 / 繁 | 中😰  | 🚫                                  | 资源同 Mobile，没必要。              | N/A                                         |
| 3   | ~~[轻之国度](https://www.lightnovel.us/)~~       | 简 / 繁 | 高🤣  | 🚫                                  | ` 需要登录 `                     | ` 轻币门槛 ` ` 导航混乱 `                           |
| 4   | [无限轻小说](https://www.8novel.com/)             | 繁     | 中😰  | ？                                   | ` 不用登录 ` ` 一章多页 `            ||
| 5   | [轻小说文库](https://www.wenku8.net/)             | 简 / 繁 | 中😰  | <img src="./merrli.png" width="36"> | ` 不用登录 ` ` 一章一页 `            ||
| 6   | ~~[轻小说百科](https://lnovel.org/)~~             | 简 / 繁 | 低😆  | 🚫                                  | ` 不用登录 ` ` 一章一页 ` ` 插图清晰度低 ` | N/A                                         |
| 7   | [真白萌](https://masiro.me/admin/novels)        | 简 / 繁 | 中😰  | <img src="./merrli.png" width="36"> | ` 一章一页 `                     | ` 需要登录 ` ` 积分购买 ` ` 等级限制 `                  |

爬虫友好度有两个重要指标：
1. 访问门槛。是否需要登陆以及积分。
2. 页面结构。一个章节多页渲染的视为中等难度。

优质的轻小说目标源标准：资源丰富，更新迅速，插图清晰，爬虫门槛合理。可以在 issue 发起补充。

其他代码参考：

- 真白萌 / 轻之国度 / 百合会旧站参考：https://github.com/ilusrdbb/lightnovel-pydownloader
- bilinovel/wenku8 参考：https://github.com/Montaro2017/bili_novel_packer

## Installation

### install from source

1. clone this repo

```bash
git clone https://github.com/lightnovel-center/linovelib2epub.git
```

2. set up a clean local python venv

> See also: [creating-virtual-environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

replace `py` with your real python command if needed. e.g. `python` or `python3`.

```bash
# Make sure you are under this project root folder: linovelib2epub/
# The following instructions are based on Windows 10.
# If you use a different os, please adjust it according to the actual situation.

# new a venv
py -m venv .venv

# activate venv
.\.venv\Scripts\activate

# install dependencies
py -m pip install -r requirements.txt

# install this package in local
python -m pip install -e .
```

### install from pypi

> 注意: 由于爬虫程序对时效非常敏感，而 pypi 发布的版本一般是滞后的，因此不推荐这种安装方式。

1. Install this package from pypi:

```
pip install linovelib2epub
```

2. update to the latest version:

```
pip install linovelib2epub --upgrade
```

## Usage

### LinovelibMobile

> target site: https://w.linovelib.com

Create a python file(e.g. `usage_demo.py`) and edit the content as follows:

```python
from linovelib2epub import Linovelib2Epub

# warning!: must run within __main__ module guard due to process spawn issue.
if __name__ == '__main__':
    linovelib_epub = Linovelib2Epub(book_id=3279)
    linovelib_epub.run()
```

If it finished without errors, you can see the epub file is under the folder where your python file is located.

LinovelibMobile is first website to be supported, and it's the default target site. So you don't need to
specify `target_site` parameter.

### Masiro

> target site: https://masiro.me

```python
from linovelib2epub import Linovelib2Epub, TargetSite

if __name__ == '__main__':
    linovelib_epub = Linovelib2Epub(book_id=1039, target_site=TargetSite.MASIRO)
    linovelib_epub.run()
```

Masiro is not the default target site, so you MUST specify `target_site` parameter as above.

And Masiro website need user login credential to view novel. You also MUST to create a config file named `.secrets.toml`
beside your python file `usage_demo.py`. For better explanation, Here's a reasonable directory organization:

```
linovelib2epub/
  ......
  .secrets.toml
  usage_demo.py
```

Then edit your `.secrets.toml` file:

```
MASIRO_LOGIN_USERNAME = '<your-masiro-username>'
MASIRO_LOGIN_PASSWORD = '<your-masiro-password>'
```

🚨 Don't leak your private account info!!! Be careful.

> Masiro 某些小说存在用户等级限制，程序执行会发生什么？

程序会给出提示，并直接退出。

> Masiro 某些小说的章节需要积分购买才能查看，程序会如何处理？

登陆后，程序会记住你的当前积分余额：

- 如果当前挑选的所有章节都是免费积分，或者你之前已经全部购买过，那么程序会直接往下执行。
- 如果当前挑选的所有章节存在需要积分购买的情况，程序会再次提示，要求做出选择，此时可以选择退出或者选择继续。

### Wenku8

> target site: https://www.wenku8.net

```python
from linovelib2epub import Linovelib2Epub, TargetSite

if __name__ == '__main__':
    linovelib_epub = Linovelib2Epub(book_id=2961, target_site=TargetSite.WENKU8)
    linovelib_epub.run()
```

Don't need login, no threshold.

## Options

| Parameters              | type    | required | default                       | description                                           |
|-------------------------|---------|----------|-------------------------------|-------------------------------------------------------|
| book_id                 | number  | YES      | None                          | 书籍 ID。                                                |
| target_site             | Enum    | NO       | `TargetSite.LINOVELIB_MOBILE` | 其他可用值参阅 TargetSite python 枚举类以及使用文档                   |
| divide_volume           | boolean | NO       | False                         | 是否分卷                                                  |
| select_volume_mode      | boolean | NO       | False                         | 选择卷模式，它为 True 时 divide_volume 强制为 True。               |
| has_illustration        | boolean | NO       | True                          | 是否下载插图                                                |
| image_download_folder   | string  | NO       | "novel_images"                | 图片下载临时文件夹. 不允许以相对路径../ 开头。                            |
| pickle_temp_folder      | string  | NO       | "pickle"                      | pickle 临时数据保存的文件夹。                                    |
| clean_artifacts         | boolean | NO       | True                          | 是否删除临时数据 / 工件，指的是 pickle 和下载的图片文件。                    |
| http_timeout            | number  | NO       | 10                            | 一个 HTTP 请求的超时等待时间 (秒)。代表 connect 和 read timeout。      |
| http_retries            | number  | NO       | 5                             | 当一个 HTTP 请求失败后，重试的最大次数。                               |
| http_cookie             | string  | NO       | ''                            | 自定义 HTTP cookie。                                      |
| custom_style_cover      | string  | NO       | ''                            | 自定义 cover.xhtml 的样式                                   |
| custom_style_nav        | string  | NO       | ''                            | 自定义 nav.xhtml 的样式                                     |
| custom_style_chapter    | string  | NO       | ''                            | 自定义每章 (?.xhtml) 的样式                                   |
| disable_proxy           | boolean | NO       | True                          | 是否禁用所在的代理环境，默认禁用                                      |
| image_download_strategy | string  | NO       | 'ASYNCIO'                     | 枚举值："ASYNCIO"、"MULTIPROCESSING"、"MULTITHREADING"（未实现） |

## Todo

- [ ] quality: setup pytest and codecov
- [ ] quality: setup more formatter and linter for maintainability
- [ ] masiro 繁体 <=> 简体

## Contributors

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/GOUKOU007"><img src="https://avatars.githubusercontent.com/u/40916324?v=4?s=60" width="60px;" alt="GokouRuri"/><br /><sub><b>GokouRuri</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3AGOUKOU007" title="Bug reports">🐛</a> <a href="https://github.com/lightnovel-center/linovelib2epub/commits?author=GOUKOU007" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/xxxfhy"><img src="https://avatars.githubusercontent.com/u/40598925?v=4?s=60" width="60px;" alt="xxxfhy"/><br /><sub><b>xxxfhy</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3Axxxfhy" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://foxlesbiao.github.io/"><img src="https://avatars.githubusercontent.com/u/41581909?v=4?s=60" width="60px;" alt="lesfox"/><br /><sub><b>lesfox</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3Afoxlesbiao" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://dongliteahouse.wordpress.com"><img src="https://avatars.githubusercontent.com/u/56831381?v=4?s=60" width="60px;" alt="Holence"/><br /><sub><b>Holence</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/commits?author=Holence" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://en.blog.nyaame.moe"><img src="https://avatars.githubusercontent.com/u/135048882?v=4?s=60" width="60px;" alt="Nikaidou Haruki"/><br /><sub><b>Nikaidou Haruki</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3Aharuki-nikaidou" title="Bug reports">🐛</a> <a href="https://github.com/lightnovel-center/linovelib2epub/commits?author=haruki-nikaidou" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://hitorinbc.com/"><img src="https://avatars.githubusercontent.com/u/33192552?v=4?s=60" width="60px;" alt="kaho"/><br /><sub><b>kaho</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3Akahosan" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Papersman"><img src="https://avatars.githubusercontent.com/u/58485012?v=4?s=60" width="60px;" alt="Papersman"/><br /><sub><b>Papersman</b></sub></a><br /><a href="https://github.com/lightnovel-center/linovelib2epub/issues?q=author%3APapersman" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Acknowledgements

- [biliNovel2Epub](https://github.com/fangxx3863/biliNovel2Epub)
