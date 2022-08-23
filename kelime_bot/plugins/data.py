from kingsozbot import oyun, rating
from pyrogram import Client, filters


@Client.on_message(filters.command("data") & filters.user("GKKurucu")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating)
