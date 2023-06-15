from Axe import *
from pyrogram import Client, filters 
from pyrogram.types import *

@AxeDL.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
        await message.reply("Just send me an artist and/or a song name and i will download music for you free!")  
