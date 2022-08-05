import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = "9248715"
api_hash = "a9c1288681c2d3265175ff96c619d064"
bot_token = "5472094867:AAGUb4aGn0bFyNKUTZlAgn7s1JozxpFifnY"

client = TelegramClient('client', api_id, api_hash)
client.start(bot_token=bot_token)

ozel_list = [5539575339]
grup_sayi = []
etiketuye = []  

@client.on(events.NewMessage(pattern='^/reload ?(.*)'))
async def chatid(event):
    global grup_sayi

@client.on(events.NewMessage())
async def chatid(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)     

@client.on(events.NewMessage(pattern='^/play@denemebot?(.*)'))
async def chatid(event):
    global grup_sayi

@client.on(events.NewMessage())
async def chatid(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)     

      
@client.on(events.NewMessage(pattern='^/statik ?(.*)'))
async def son_durum(event):
    global grup_sayi,ozel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**botun grup sayısı 🧐**\n\nToplam Grup: `{len(grup_sayi)}`")


@client.on(events.NewMessage(pattern='^/reklam ?(.*)'))
async def reklam(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a reklam gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 @deepkral **\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi reklamınız.")


print(">> Bot çalıyor merak etme  <<")
client.run_until_disconnected() 
