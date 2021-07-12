


import requests
from pyrogram import Client as Bot

from EivaMusic.config import API_HASH
from EivaMusic.config import API_ID
from EivaMusic.config import BG_IMAGE
from EivaMusic.config import BOT_TOKEN
from EivaMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="EivaMusic.modules"),
)

bot.start()
run()
