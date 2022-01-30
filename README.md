<html>
<div align="center">
<img src="https://camo.githubusercontent.com/48b5c67f0baa5b41fc98c96dad8de4771b0fc583d6b3dda417c7f8e01e801028/68747470733a2f2f692e696d6775722e636f6d2f734a7a665a734c2e6a7067" alt="alt text" width="250" height="250"></img>
</div>
<h1 align="center">@danielaceros
<div align="center">
<a href=https://github.com/danielaceros><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=@danielaceros&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<img src="https://img.shields.io/github/followers/danielaceros?style=social" alt="Star Badge"/>
<a><img src="https://img.shields.io/github/last-commit/danielaceros/instaloaderbot" alt="Join Community Badge"/></a>
<a><img src="https://img.shields.io/github/repo-size/danielaceros/instaloaderbot" />
</div>
</html>

# instaloaderbot
A telegram bot who gets some informations and pics from Instagram. It can dowload everything like posts, highlights, stories and even more.
## Getting Started
First of all, you should dowload de repo, or even de script, 'instaloader.py' and put it in an empty folder. Later, you should install the needed modules, via 'pip/pip3 install'
```bash
pip/pip3 install instaloader
pip/pip3 install logging
pip/pip3 install os
pip/pip3 install requests
pip/pip3 install shutil
pip/pip3 install instaloader
pip/pip3 install pandas
pip/pip3 install itertools
pip/pip3 install python-telegram-bot
```
## Telegram BOT
You need to create a BOT on TELEGRAM, for this, you can chat to 'BotFather', then '/newbot', and follow the instructions, then, when you have created it, you need to copy the API KEY that BotFather gives to you and put it on the script, in the part of 'Updater('' #insert your BOT API KEY)'.
Later, you have to add commands, for this, return to 'BotFather', '/mybots', select your bot, 'Edit Bot', 'Edit Commands', then you paste this list:
```
login - LOGIN [user] [password]
posts - Get USER'S POSTS [user] [nº] [a/d](ascendent/descentent)
postsdate -Get USER'S POSTS by DATE [user] [nº] [since(d/m/y)] [until(d/m/y)] [asc/desc](ascendent/descentent)
top - Get TOP POST of USER [user] [nº]
profilepic - Get PROFILE PIC of an USER [user]
stories -Get an USER STORY [user]
highlights - Get USER'S HIGHLIGHTS [user] [nº]
tagged - Get tagged POSTS of an USER [user] [nº]
story - Get USER'S STORIES [nº]
feed - Get USER'S FEED [nº]
followers - Get USER'S FOLLOWERS [user] [nº]
following - Get USER'S FOLLOWING [user] [nº]
mutual - Get MUTUAL FOLLOWERS/FOLLOWING [user] [nº]
similar - Get similar ACCOUNTS [user] [nº]
clear - CLEAR all FILES
```
## Running CODE
When you have created the BOT, installed the packages, and gived to the '.py' your API TOKEN, you can run the code by an IDE or PowerShell/CommandPrompt by:
```bash
python instaloaderbot.py
python3 instaloaderbot.py
```
