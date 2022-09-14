from kelime_bot import oyun, rating
from pyrogram import Client, filters


@Client.on_message(filters.command("data") & filters.user("@realjihokimin")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating)
