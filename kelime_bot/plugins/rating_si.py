from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("reytinq"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """📝 Qruplar üzrə ən yaxşı oyunçular

"""
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan}  Puan\n"
                eklenen += 1
                if eklenen == 20:
                    break
                
    await c.send_message(m.chat.id, metin)
