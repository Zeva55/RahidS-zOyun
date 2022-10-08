from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("reytinq"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """📝 Qlobal qruplar üzrə ən yaxşı oyunçular

"""

${(top).sort((a, b) => b.score - a.score).slice(0, 20).map((member, index) => `${["🥇","🥈","🥉"][index] || "🎲"} ${index + 1}) <b><i>${member.firstName} → ${member.score} ${HusnuEhedov(member.score, "puan", "puan", "puan")}</i></b>`).join("\n")}
                `))
            }
        }
    })
})
                
    await c.send_message(m.chat.id, metin)
