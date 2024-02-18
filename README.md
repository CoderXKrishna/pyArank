# py-Arank Library

Core library of [The Arank](https://github.com/CoderXKrishna/Arank), a python based telegram userbot.

[![CodeFactor](https://www.codefactor.io/repository/github/CoderXKrishna/pyArank/badge)](https://www.codefactor.io/repository/github/CoderXKrishna/pyArank)
[![PyPI - Version](https://img.shields.io/pypi/v/py-Arank?style=round)](https://pypi.org/project/py-Arank)    
[![PyPI - Downloads](https://img.shields.io/pypi/dm/py-Arank?label=DOWNLOADS&style=round)](https://pypi.org/project/py-Arank)    
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/CoderXKrishna/Arank/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/CoderXKrishna/Arank)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

# Installation
```bash
pip3 install -U py-Arank
```

# Usage
- Create folders named `plugins`, `addons`, `assistant` and `resources`.   
- Add your plugins in the `plugins` folder and others accordingly.   
- Create a `.env` file with following mandatory Environment Variables
   ```
   API_ID
   API_HASH
   SESSION
   REDIS_URI
   REDIS_PASSWORD
   ```
- Check
[`.env.sample`](https://github.com/CoderXKrishna/Arank/blob/main/.env.sample) for more details.   
- Run `python3 -m pyArank` to start the bot.   

## Creating plugins
 - ### To work everywhere

```python
@Arank_cmd(
    pattern="start"
)   
async def _(e):   
    await e.eor("Arank Started!")   
```

- ### To work only in groups

```python
@Arank_cmd(
    pattern="start",
    groups_only=True,
)   
async def _(e):   
    await eor(e, "Arank Started.")   
```

- ### Assistant Plugins 👇

```python
@asst_cmd("start")   
async def _(e):   
    await e.reply("Arank Started.")   
```

See more working plugins on [the offical repository](https://github.com/CoderXKrishna/Arank)!

> Made with 💕 by [@CoderXKrishna](https://t.me/CoderXKrishna).    


# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Arank is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

# Credits
* [![CoderXKrishna-Devs](https://img.shields.io/static/v1?label=CoderXKrishna&message=devs&color=critical)](https://t.me/Carding_Chronicle)
