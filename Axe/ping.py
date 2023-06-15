from time import time
from datetime import datetime

from pyrogram.types import *
from pyrogram import Client, filters, emoji


@Client.on_message(filters.command("ping"))
async def ping_pong(client: Client, m: Message):
    start = time()
    m_reply = await m.reply_text("**checking ping ⚡**")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"{emoji.PING_PONG} `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )

   




