<html>
<div align="center">
<img src="https://static.wikia.nocookie.net/apple/images/7/79/Siri_%28logo%29.png/revision/latest?cb=20200715180213&path-prefix=es" alt="alt text" width="250" height="250"></img>
</div>
<h1 align="center">@danielaceros
<div align="center">
<a href=https://github.com/danielaceros><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=@danielaceros&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<img src="https://img.shields.io/github/followers/danielaceros?style=social" alt="Star Badge"/>
<a><img src="https://img.shields.io/github/last-commit/danielaceros/namerecognition" alt="Join Community Badge"/></a>
<a><img src="https://img.shields.io/github/repo-size/danielaceros/namerecognition" />
</div>
</html>

# namerecognition
A telegram bot who recognizes some stuff you need like your neem for online clases, and notify you by Telegram
## Getting Started
First of all, you should dowload de repo, or even de script, 'instaloader.py' and put it in an empty folder. Later, you should install the needed modules, via 'pip/pip3 install'
```bash
pip/pip3 install requests
pip/pip3 install python-telegram-bot
pip/pip3 install speech_recognition
pip/pip3 install logging
```
## Telegram BOT
You need to create a BOT on TELEGRAM, for this, you can chat to 'BotFather', then '/newbot', and follow the instructions, then, when you have created it, you need to copy the API KEY that BotFather gives to you and put it on the script, in the part of 'Updater('' #insert your BOT API KEY)'.
Later, you have to add commands, for this, return to 'BotFather', '/mybots', select your bot, 'Edit Bot', 'Edit Commands', then you paste this list:
```
listen - TO only LISTEN if your name is not present
```
## Running CODE
When you have created the BOT, installed the packages, and gived to the '.py' your API TOKEN, you can run the code by an IDE or PowerShell/CommandPrompt by:
```bash
python recognition.py
python3 recognition.py
```
