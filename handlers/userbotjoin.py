import asyncio

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant

from config import SUDO_USERS, ASSISTANT_NAME
from helpers.decorators import authorized_users_only, errors
from callsmusic import client as USER


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝙰𝚍𝚍 𝙼𝚎 𝙰𝚜 𝙰𝚍𝚖𝚒𝚗 𝙵𝚒𝚛𝚜𝚝 𝚂𝚝𝚞𝚙𝚒𝚍.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DemonMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "𝙸 𝙹𝚘𝚒𝚗𝚎𝚍 𝙷𝚎𝚛𝚎 𝙰𝚜 𝚈𝚘𝚞 𝚁𝚎𝚚𝚞𝚎𝚜𝚝𝚎𝚍..")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>𝙰𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝙰𝚕𝚛𝚎𝚊𝚍𝚢 𝙷𝚎𝚛𝚎 𝙳𝚎𝚊𝚛..</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr manually add @s4shivxassistant to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>𝙼𝚢 𝙰𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝 𝙹𝚘𝚒𝚗𝚎𝚍...𝙽𝚘𝚠 𝙸𝚝𝚜 𝚂𝚑𝚘𝚠 𝚃𝚒𝚖𝚎..</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>𝚄𝚗𝚊𝚋𝚕𝚎 𝚃𝚘 𝙻𝚎𝚊𝚟𝚎 ...𝙽𝚘𝚝 𝙺𝚗𝚘𝚠 𝚆𝚑𝚢 ..𝙺𝚒𝚌𝚔 𝙼𝚊𝚗𝚞𝚊𝚕𝚕𝚢.</b>",
        )
        return


@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"𝙷𝚎𝚕𝚙𝚎𝚛 𝙻𝚎𝚊𝚟𝚒𝚗𝚐... 𝙻𝚎𝚏𝚝: {left} 𝚌𝚑𝚊𝚝𝚜. 𝙵𝚊𝚒𝚕𝚎𝚍: {failed} 𝚌𝚑𝚊𝚝𝚜."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"𝙷𝚎𝚕𝚙𝚎𝚛 𝙻𝚎𝚊𝚟𝚒𝚗𝚐... 𝙻𝚎𝚏𝚝: {left} 𝚌𝚑𝚊𝚝𝚜. 𝙵𝚊𝚒𝚕𝚎𝚍: {failed} 𝚌𝚑𝚊𝚝𝚜."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"𝙻𝚎𝚏𝚝 {left} 𝚌𝚑𝚊𝚝𝚜. 𝙵𝚊𝚒𝚕𝚎𝚍 {failed} 𝚌𝚑𝚊𝚝𝚜."
        )


@Client.on_message(
    filters.command(["userbotjoinchannel", "ubjoinc"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
        conchat = await client.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("Is chat even linked")
        return
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>𝙰𝚍𝚍 𝙼𝚎 𝙰𝚜 𝙰𝚍𝚖𝚒𝚗 𝙵𝚒𝚛𝚜𝚝 𝚂𝚝𝚞𝚙𝚒𝚍</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DemonMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>𝙰𝚜𝚜𝚒𝚝𝚊𝚗𝚝 𝙰𝚕𝚛𝚎𝚊𝚍𝚢 𝙷𝚎𝚛𝚎 𝙳𝚎𝚊𝚛..</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nOr manually add @s4shivxassistant to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
