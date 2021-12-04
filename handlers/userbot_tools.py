import asyncio
from helpers.legend import user
from pyrogram.types import Message
from pyrogram import Client, filters
from config import BOT_USERNAME, SUDO_USERS
from helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only, sudo_users_only


@Client.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "𝙃𝙚𝙮 𝙈𝙮 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙄𝙨 𝙅𝙤𝙞𝙣𝙚𝙙. 𝙃𝙪𝙧𝙧𝙧𝙚𝙮 🐬🤞  ")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, " 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙝𝙚𝙧𝙚 ..𝙅𝙪𝙨𝙩 𝙏𝙮𝙥𝙚 𝙖𝙣𝙙 𝙋𝙡𝙖𝙮😋")
        return await user.send_message(chat_id, "𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙝𝙚𝙧𝙚 ..𝙅𝙪𝙨𝙩 𝙏𝙮𝙥𝙚 𝙖𝙣𝙙 𝙋𝙡𝙖𝙮😋")


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def leave_chat(_, m: Message):
    chat_id = m.chat.id
    try:
        await user.leave_chat(chat_id)
        return await _.send_message(
            chat_id,
            "✅ 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙇𝙚𝙖𝙫𝙚𝙙 𝘾𝙝𝙖𝙩𝙨",
        )
    except UserNotParticipant:
        return await _.send_message(
            chat_id,
            "❌ 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙇𝙚𝙖𝙫𝙚𝙙 𝘾𝙝𝙖𝙩𝙨",
        )


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩** 𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝘾𝙝𝙖𝙩𝙨 !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝘼𝙡𝙡 𝙂𝙧𝙤𝙪𝙥...\n𝙇𝙚𝙛𝙩: {left} 𝙘𝙝𝙖𝙩𝙨.\n𝙁𝙖𝙞𝙡𝙚𝙙: {failed} 𝙘𝙝𝙖𝙩𝙨."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙇𝙚𝙖𝙫𝙞𝙣𝙜...\n𝙇𝙚𝙛𝙩: {left} 𝘾𝙝𝙖𝙩𝙨.\n𝙁𝙖𝙞𝙡𝙚𝙙: {failed} 𝙘𝙝𝙖𝙩𝙨."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ 𝙇𝙚𝙛𝙩 𝙛𝙧𝙤𝙢: {left} 𝙘𝙝𝙖𝙩𝙨.\n❌ 𝙁𝙖𝙞𝙡𝙚𝙙 𝙞𝙣: {failed} 𝙘𝙝𝙖𝙩𝙨."
    )


@Client.on_message(filters.left_chat_member)
async def ubot_leave(c: Client, m: Message):
    ass_id = (await user.get_me()).id
    bot_id = (await c.get_me()).id
    chat_id = m.chat.id
    left_member = m.left_chat_member
    if left_member.id == bot_id:
        await user.leave_chat(chat_id)
    elif left_member.id == ass_id:
        await c.leave_chat(chat_id)