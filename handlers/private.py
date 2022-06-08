from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADRQIAAhHHQFSfHJ-IR0eN6gI")
    await message.reply_text(
        f"""**- 𝙃𝙚𝙮 𝘼𝙢 {𝙈𝙀𝙉𝙏𝘼𝙇 𝙭 𝙌𝙐𝙀𝙀𝙉} 💛🐬,
- 𝙄 𝙘𝙖𝙣 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥'𝙨 𝙫𝙤𝙞𝙘𝙚 𝙘𝙖𝙡𝙡. 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙙 𝙗𝙮 [𝙈𝙀𝙉𝙏𝘼𝙇](https://t.me/OFFICIAL_MENTALMOD) 💛🤞.

𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙜𝙧𝙤𝙪𝙥 𝙖𝙣𝙙 𝙥𝙡𝙖𝙮 𝙢𝙪𝙨𝙞𝙘 𝙛𝙧𝙚𝙚𝙡𝙮 🐬💕**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         " 𝙊𝙬𝙣𝙚𝙧 ", url="https://t.me/OFFICIAL_MENTALMOD")
                  ],[
                    InlineKeyboardButton(
                        "😈  𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/A_4_AMAN_0fficcial"
                    ),
                    InlineKeyboardButton(
                        "✌️ 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/MENTAL_MOD"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝘼𝙙𝙙 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ➕", url="https://t.me/MENTALxQUEEN_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 𝙈𝙀𝙉𝙏𝘼𝙇 𝙭 𝙌𝙐𝙀𝙀𝙉 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧 𝙄𝙨 𝙊𝙣𝙡𝙞𝙣𝙚 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝙈𝙖𝙣𝙖𝙜𝙚𝙧", url="https://t.me/A_4_AMAN_Officcial")
                ]
            ]
        )
   )


