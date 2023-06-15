from pyrogram import Client, filters 
from pyrogram.types import *

@Client.on_message(filters.private & filters.command("start"))
async def start(client: Client, message: Message):
        await message.reply("Hey!")
 
