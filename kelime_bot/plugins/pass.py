from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 30:
            oyun[m.chat.id]["kec"] += 1
            await c.send_message(m.chat.id,f"❗ Sizin tam yol haqqınız var!\n➡️ Sözü keçdim !\n✏️ Doğru söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🔎 ǫᴀʀışıǫ söᴢʟəʀi ᴛᴀᴘ

🎯 ʀᴀᴜɴᴅ: {oyun[m.chat.id]['round']}/100 
ℹ️ ᴛᴀᴘıʟᴀᴄᴀǫ söᴢ: <code>{kelime_list}</code>
💰 ǫᴀᴢᴀɴᴅɪɢ̆ɪɴ xᴀʟ: 50
📄 ᴜᴢᴜɴʟᴜǫ: {int(len(kelime_list)/2)} 
💡 ɪʟᴋ ʜəʀғ: {oyun[m.chat.id]["kelime"][0]}

@Cenublar qrupumuza dəvətlisiniz❤️
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçid düzgün saxlanıldı! </code> \n Oyunu dayandırmaq üçün /dayan yazın ✍🏻**")
    else:
        await m.reply(f"❗ **Qrupda aktiv oyun yoxdur!\n Yeni oyuna başlamaq üçün /oyna yazın ✍🏻**")
