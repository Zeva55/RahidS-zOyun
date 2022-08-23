from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kingsozbot import USERNAME
from pyrogram.types import Message
from kingsozbot.helpers.keyboards import *
from kingsozbot.helpers.kelimeler import kelime_sec
from kingsozbot import *



@Client.on_message(filters.command("dayan") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** Tərəfindən Oyun dayandırıldı\n\nYeni Oyuna Başlamaq Üçün /oyna Yaza Bilərsən\n\n 📝 Xallar səyfəsi  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
