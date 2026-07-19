# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from pyrogram.types import InputMediaPhoto
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.errors import FloodWait, UserNotParticipant

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
import io
import shutil 
from contextlib import redirect_stdout, redirect_stderr
from pymongo import DESCENDING

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import sys
import platform
import random
import psutil

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import time
import gc
import asyncio 
import traceback
import speedtest
import logging
logging.basicConfig(level=logging.INFO)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

IMAGES = [
    "https://graph.org/file/98245197c3a4185b49dbe-3df65fb012e4195cff.jpg",
    "https://graph.org/file/27dd5451f160ce28dadd4-8ca0a7d6480451adc8.jpg",
    "https://graph.org/file/0e77ba48a8b7a3b09296f-362372bee0d84fd217.jpg"
]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from database import (
    save_file,
    get_file,
    increase_download,
    add_user,
    get_all_users,
    total_users,
    total_files, 
    total_admins,
    add_admin_db,
    remove_admin_db,
    is_admin,
    get_all_admins,
    add_force_sub,
    remove_force_sub,
    get_force_subs,
    files,
    users,
    verify_db,
    save_verify,
    get_verify,
    delete_verify,
    ban_user,
    unban_user,
    is_banned,
    get_file_by_unique_id,
    today_files,
    week_files,
    storage_used,
    top_uploaders,
    export_database,
    database_info,
    import_database
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from keep_alive import keep_alive

START_TIME = time.time()
BOT_VERSION = "v3.0"
CACHE = {}
MAINTENANCE = False

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def format_size(size):
    power = 1024
    units = ["B", "KB", "MB", "GB", "TB"]

    n = 0
    while size > power and n < len(units) - 1:
        size /= power
        n += 1

    return f"{size:.2f} {units[n]}"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

app = Client(
    "filelinkbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
) 

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def send_log(text):
    try:
        await app.send_message(
            LOG_CHANNEL,
            text,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(e)
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import base64
import re

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

BATCH_USERS = {}
INDEX_CACHE = {}

# ------------------------- #
# INDEX SYSTEM
# ------------------------- #

LETTERS = [
    "A","B","C","D","E","F","G",
    "H","I","J","K","L","M","N",
    "O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
]

# ================= GET MESSAGE ID =================

async def get_message_id(client, link):

    try:
        link = link.strip()

        if "/c/" in link:

            parts = link.split("/")

            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1])

            return chat_id, msg_id

        match = re.search(r"t\.me/([^/]+)/(\d+)", link)

        if match:

            username = match.group(1)
            msg_id = int(match.group(2))

            chat = await client.get_chat(username)

            return chat.id, msg_id

        return None, None

    except:
        return None, None


# ================= BATCH COMMAND =================

@app.on_message(filters.command("batch") & filters.private)
async def batch_command(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 You are banned from using this bot."
        )

    user_id = message.from_user.id

    if user_id != OWNER_ID and not await is_admin(user_id):

        return await message.reply_text(
            "ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃."
        )

    BATCH_USERS[user_id] = {
        "step": "first"
    }

    await message.reply_text(
        "🔗 Gɪᴠᴇ Mᴇ Bᴀᴛᴄʜ Fɪʀsᴛ Mᴇssᴀɢᴇ 𝗟𝗶𝗻𝗸 ғʀᴏᴍ ʏᴏᴜʀ 𝗗𝗕 ᴄʜᴀɴɴᴇʟ"
    )


# ================= HANDLE BATCH =================

@app.on_message(
    filters.private &
    filters.text &
    ~filters.command([
        "start",
        "batch",
        "stats",
        "broadcast",
        "addadmin",
        "removeadmin",
        "adminlist",
        "addfsub",
        "removefsub",
        "fsublist",
        "index",
        "ban",
        "unban",
        "banlist",
        "alive",
        "id",
        "system", 
        "restart",
        "clearcache",
        "fileinfo",
        "privacy",
        "version",
        "support",
        "storage",
        "backupdb",
        "restoredb",
        "cleanup",
        "analysis",
        "speedtest",
        "filestats",
        "dbinfo"
    ])
)
async def handle_batch(client, message):

    user_id = message.from_user.id

    if user_id not in BATCH_USERS:
        return

    data = BATCH_USERS[user_id]

    # FIRST LINK
    if data["step"] == "first":

        chat_id, first_msg_id = await get_message_id(
            client,
            message.text
        )

        if not first_msg_id:

            return await message.reply_text(
                "‼️ Iɴᴠᴀʟɪᴅ Fɪʀsᴛ Lɪɴᴋ"
            )

        data["chat_id"] = chat_id
        data["first_msg_id"] = first_msg_id
        data["step"] = "last"

        return await message.reply_text(
            "🔗 Gɪᴠᴇ Mᴇ Bᴀᴛᴄʜ Lᴀsᴛ Mᴇssᴀɢᴇ 𝗟𝗶𝗻𝗸 ғʀᴏᴍ ʏᴏᴜʀ 𝗗𝗕 ᴄʜᴀɴɴᴇʟ"
        )

    # LAST LINK
    elif data["step"] == "last":

        chat_id, last_msg_id = await get_message_id(
            client,
            message.text
        )

        if not last_msg_id:

            return await message.reply_text(
                "‼️ Iɴᴠᴀʟɪᴅ Lᴀsᴛ Lɪɴᴋ"
            )

        first_msg_id = data["first_msg_id"]

        if last_msg_id < first_msg_id:

            return await message.reply_text(
                "‼️ Lᴀsᴛ ᴍᴇssᴀɢᴇ ᴍᴜsᴛ ʙᴇ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ ғɪʀsᴛ ᴍᴇssᴀɢᴇ"
            )

        batch_data = (
            f"batch:{data['chat_id']}:{first_msg_id}:{last_msg_id}"
        )

        encoded = base64.urlsafe_b64encode(
            batch_data.encode("utf-8")
        ).decode("utf-8")

        bot_username = (await client.get_me()).username

        link = f"https://t.me/{bot_username}?start={encoded}"

        await message.reply_text(
            f"✅ ʙᴀᴛᴄʜ ʟɪɴᴋs ɢᴇɴᴇʀᴀᴛᴇᴅ\n\n{link}"
        )

        del BATCH_USERS[user_id]

# ------------------------- #
# FORCE SUBSCRIBE CHECK
# ------------------------- #

async def check_force_sub(client, user_id):

    channels = await get_force_subs()

    if not channels:
        return True, None

    buttons = []

    for channel in channels:

        try:
            chat = await client.get_chat(channel)
        except Exception:
            # Invalid/deleted channel in DB
            try:
                await remove_force_sub(channel)
            except:
                pass
            continue

        try:
            member = await client.get_chat_member(chat.id, user_id)

            if member.status in (
                ChatMemberStatus.LEFT,
                ChatMemberStatus.BANNED
            ):
                raise UserNotParticipant

        except UserNotParticipant:

            if chat.username:
                link = f"https://t.me/{chat.username}"
            else:
                try:
                    invite = await client.create_chat_invite_link(
                        chat.id,
                        member_limit=1
                    )
                    link = invite.invite_link
                except:
                    continue

            buttons.append([
                InlineKeyboardButton(
                    chat.title,
                    url=link
                )
            ])

        except Exception:
            continue

    if buttons:
        buttons.append([
            InlineKeyboardButton(
                "• ᴛʀʏ ᴀɢᴀɪɴ •",
                callback_data="checksub"
            )
        ])

        return False, InlineKeyboardMarkup(buttons)

    return True, None
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# START + LINK HANDLER
@app.on_message(filters.command("start"))
async def start(client, message: Message):

    user_id = message.from_user.id

    if await is_banned(user_id):
        return await message.reply_text(
            "🚫 **You are banned from using this bot.**\n\n"
            "**If you believe this is a mistake, contact the "
            "[Owner](https://t.me/Mr_Mohammed_29).**",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

    await add_user(user_id)

    # Save parameter before Force Subscribe check
    if len(message.command) > 1:
        param = message.command[1]
        await save_verify(user_id, param)

    user = message.from_user

    await send_log(
        f"**ɴᴇᴡ ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ**\n\n"
        f"👤 **{user.first_name}**\n"
        f"🆔 **`{user.id}`**\n"
        f"📛 **@{user.username if user.username else 'None'}**"
    )

    # ------------------------- #
    # FORCE SUBSCRIBE CHECK
    # ------------------------- #

    ok, keyboard = await check_force_sub(
        client,
        user_id
    )

    if not ok:
        return await message.reply_photo(
            photo=FORCE_SUB_IMAGE,
            caption=(
                "**›› ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ...**\n\n"
                "• ᴘʀᴇss **ᴛʀʏ ᴀɢᴀɪɴ**."
            ),
            reply_markup=keyboard,
            parse_mode=ParseMode.MARKDOWN
        )

    # START ANIMATION
    m = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
    await asyncio.sleep(0.5)
    await m.edit_text("🔥")
    await asyncio.sleep(0.5)
    await m.edit_text("⚡")
    await asyncio.sleep(0.5)
    await m.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
    await asyncio.sleep(0.5)
    await m.delete()

    if len(message.command) > 1:
        param = message.command[1]

        # ================= BATCH LINK =================

        try:

            decoded = base64.urlsafe_b64decode(
                param + "=" * (-len(param) % 4)
            ).decode("utf-8", errors="ignore")

            if decoded.startswith("batch:"):

                _, chat_id, first_id, last_id = decoded.split(":")

                chat_id = int(chat_id)
                first_id = int(first_id)
                last_id = int(last_id)

                sent_messages = []

                wait = await message.reply_text("⏳ sᴇɴᴅɪɴɢ ғɪʟᴇs...")

                for msg_id in range(first_id, last_id + 1):

                    try:
                        msg = await client.get_messages(chat_id, msg_id)

                        if not msg:
                            continue

                        original_caption = msg.caption if msg.caption else ""

                        caption = (
                            f"**{original_caption}**\n\n"
                            f"**›› ʙʏ :** [ᴀᴇʀᴏ ᴜɴɪᴛʏ](https://t.me/Aero_Unity)"
                        )

                        buttons = InlineKeyboardMarkup(
                            [[InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity")]]
                        )

                        if msg.video:
                            sent = await message.reply_video(
                                video=msg.video.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                supports_streaming=True,
                                parse_mode=ParseMode.MARKDOWN
                            )

                        elif msg.audio:
                            sent = await message.reply_audio(
                                audio=msg.audio.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                parse_mode=ParseMode.MARKDOWN
                            )

                        elif msg.document:
                            sent = await message.reply_document(
                                document=msg.document.file_id,
                                caption=caption,
                                reply_markup=buttons,
                                parse_mode=ParseMode.MARKDOWN
                            ) 

                        elif msg.sticker:
                            sent = await message.reply_sticker(sticker=msg.sticker.file_id)

                        elif msg.animation:
                           sent = await message.reply_animation(
                               animation=msg.animation.file_id,
                               caption=caption,
                               reply_markup=buttons,
                               parse_mode=ParseMode.MARKDOWN
                           )
                        else:
                            continue

                        sent_messages.append(sent)

                        try:
                            unique_id = None

                            if msg.video:
                                unique_id = msg.video.file_unique_id
                            elif msg.document:
                                unique_id = msg.document.file_unique_id
                            elif msg.audio:
                                unique_id = msg.audio.file_unique_id
                            elif msg.animation:
                                unique_id = msg.animation.file_unique_id

                            if unique_id:
                                await increase_download(unique_id)

                        except Exception:
                           pass

                        await asyncio.sleep(0.3)

                    except Exception as e:
                        print(e)

                await wait.delete()

                await send_log(
                    f"📦 **Bᴀᴛᴄʜ Aᴄᴄᴇss**\n\n"
                    f"👤 {message.from_user.mention}\n"
                    f"🆔 `{message.from_user.id}`\n"
                    f"Messages: {first_id} - {last_id}"
                )

                warn = await message.reply_text(
                    " **⏳ Dᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs...**\n\n"
                    " **›› Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ 𝟻 ᴍɪɴᴜᴛᴇs.**\n"
                    " **›› Sᴏ ᴘʟᴇᴀsᴇ sᴀᴠᴇ ᴛʜᴇᴍ.**",
                    parse_mode=ParseMode.MARKDOWN
                )

                await asyncio.sleep(300)

                for x in sent_messages:
                    try:
                        await x.delete()
                    except:
                        pass

                try:
                    await warn.delete()
                except:
                    pass
 
                return

        except Exception as e:
            return

        file_unique_id = message.command[1]
        data = await get_file(file_unique_id)

        if not data:
            return await message.reply_text("🔎 Fɪʟᴇ Is Nᴏᴛ Fᴏᴜɴᴅ, Cᴏɴᴛᴀᴄᴛ Tᴏ Oᴡɴᴇʀ.")

        original_caption = data.get("caption", "")
        caption = (
    f"**{original_caption}**\n\n"
    f"**›› ʙʏ :[ᴀᴇʀᴏ ᴜɴɪᴛʏ](https://t.me/Aero_Unity)**"
)

        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity")]]
        )

        if data.get("file_type") == "video":
            sent = await message.reply_video(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                thumb=data.get("thumb") if data.get("thumb") else None,
                supports_streaming=True,
                parse_mode=ParseMode.MARKDOWN
        ) 

        elif data.get("file_type") == "audio":
            sent = await message.reply_audio(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        elif data.get("file_type") == "document":
            sent = await message.reply_document(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        elif data.get("file_type") == "sticker":
            sent = await message.reply_sticker(
                data["file_id"]
        )

        elif data.get("file_type") == "animation":  # GIF
            sent = await message.reply_animation(
                data["file_id"],
                caption=caption,
                reply_markup=buttons,
                parse_mode=ParseMode.MARKDOWN
        )

        else:
            return await message.reply_text("‼️ Unsupported format")

        await increase_download(file_unique_id)

        await delete_verify(user_id)

        await send_log(
            f"📥 **Fɪʟᴇ Aᴄᴄᴇssᴇᴅ**\n\n"
            f"👤 {message.from_user.mention}\n"
            f"🆔 `{message.from_user.id}`\n"
            f"📂 {data.get('caption','No Caption')}"
        )

        warn = await message.reply_text(
    " **⏳ Dᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs...**\n\n"
    " **›› Yᴏᴜʀ ғɪʟᴇs ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴡɪᴛʜɪɴ 𝟻 ᴍɪɴᴜᴛᴇs.**\n"
    " **›› Sᴏ ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜᴇᴍ ᴛᴏ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇs.**\n\n"
    " ›› 𝗡𝗼𝘁𝗲: ᴜsᴇ **𝗩𝗟𝗖 𝗣𝗹𝗮𝘆𝗲𝗿** ᴏʀ **𝗠𝗫 𝗣𝗹𝗮𝘆𝗲𝗿** ғᴏʀ ʙᴇsᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ.",
    parse_mode=ParseMode.MARKDOWN
        )

        # AFTER FILE ANIMATION
        m2 = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
        await asyncio.sleep(0.4)
        await m2.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
        await asyncio.sleep(0.5)
        await m2.delete()

        await asyncio.sleep(300)

        try:
            await sent.delete()
        except:
            pass

        try:
            await warn.delete()
        except:
            pass

        return

    # START MESSAGE WITH BUTTONS
    photo = random.choice(IMAGES)

    await message.reply_photo(
        photo=photo,
        caption=(
            "𝗛𝗲𝗹𝗹𝗼 ♡,\n\n"
            "›› 𝗜 𝗰𝗮𝗻 𝘀𝘁𝗼𝗿𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗮𝗰𝗰𝘀𝘀 𝗶𝘁 𝗳𝗿𝗼𝗺 𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗹𝗶𝗻𝗸."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity"),
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/Mr_Mohammed_29")
                ]
            ]
        ),
        parse_mode=ParseMode.MARKDOWN
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ONLY OWNER + ADMIN CAN UPLOAD 
@app.on_message(
    (filters.document | filters.video | filters.audio | filters.sticker | filters.animation) &
    filters.private
)
async def save_media(client, message: Message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 You are banned from using this bot."
        )

    # Allow only owner + admin
    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text(" ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")

    original_caption = message.caption if message.caption else ""

    # Detect file type
    if message.video:
        file = message.video
        file_type = "video"
        thumb = None
        if hasattr(file, "thumbs") and file.thumbs:
            thumb = file.thumbs[-1].file_id

    elif message.audio:
        file = message.audio
        file_type = "audio"
        thumb = None

    elif message.document:
        file = message.document
        file_type = "document"
        thumb = None

    elif message.sticker:
        file = message.sticker
        file_type = "sticker"
        thumb = None

    elif message.animation:  # GIF
        file = message.animation
        file_type = "animation"
        thumb = None

    else:
        return await message.reply_text("‼️ Uɴsᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛ")

    file_id = file.file_id
    file_unique_id = file.file_unique_id

    await save_file(
        file_id=file_id,
        file_unique_id=file_unique_id,
        file_type=file_type,
        caption=original_caption,
        thumb=thumb,
        file_name=getattr(file, "file_name", ""),
        file_size=getattr(file, "file_size", 0),
        uploader_id=message.from_user.id
    )

    await send_log(
        f"📤 **Nᴇᴡ Fɪʟᴇ Uᴘʟᴏᴀᴅᴇᴅ**\n\n"
        f"👤 {message.from_user.mention}\n"
        f"🆔 `{message.from_user.id}`\n"
        f"📁 {getattr(file, 'file_name', file_type)}"
    )

    link = f"https://t.me/{BOT_USERNAME}?start={file_unique_id}"

    await message.reply_text(f"🔗 𝗛𝗲𝗿𝗲 𝗜𝘀 𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸:\n{link}")
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# STATS
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(client, message: Message):

    start = time.time()
    total = await total_users()

    uptime_seconds = int(time.time() - START_TIME)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    ping = round((time.time() - start) * 1000)

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ", callback_data="refresh_stats")]]
    )

    process = psutil.Process()
    memory = process.memory_info().rss / (1024 * 1024)

    await message.reply_text(
        f"📊 **𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀**\n\n"
        f"👥 Usᴇʀs: {total}\n"
        f"⏱ Uᴘᴛɪᴍᴇ: {hours}h {minutes}m {seconds}s\n"
        f"⚡ Pɪɴɢ: {ping} ms\n"
        f"🧠 Mᴇᴍᴏʀʏ Usᴀɢᴇ: {memory:.2f} MB\n"
        f"🧾 Vᴇʀsɪᴏɴ: {BOT_VERSION}",
        reply_markup=keyboard
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# BROADCAST
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text("Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ..")

    msg = message.reply_to_message

    users = await get_all_users()

    sent = 0
    failed = 0

    status = await message.reply_text("⏳️ 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱.....")  

    for user_id in users:
        try:
            await msg.copy(chat_id=int(user_id))
            sent += 1
            await asyncio.sleep(0.05)

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception as e:
            failed += 1
            print(f"Failed: {user_id} | {e}")

    await status.edit_text(
        f"⏳️ 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱\n\n"
        f"◇ Sᴜᴄᴄᴇssғᴜʟ: {sent}\n"
        f"◇ Uɴsᴜᴄᴄᴇssғᴜʟ: {failed}"
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
    
@app.on_message(
    filters.private &
    ~filters.service &
    ~filters.command([
        "start",
        "batch",
        "stats",
        "broadcast",
        "addadmin",
        "removeadmin",
        "adminlist",
        "addfsub",
        "removefsub",
        "fsublist",
        "index",
        "ban",
        "unban",
        "banlist",
        "alive",
        "id",
        "system",
        "restart",
        "clearcache",
        "fileinfo",
        "privacy",
        "version",
        "support",
        "storage",
        "backupdb",
        "restoredb",
        "cleanup",
        "analysis",
        "speedtest",
        "filestats",
        "dbinfo"
    ])
)
async def auto_add_user(client, message):

    if message.from_user and await is_banned(message.from_user.id):
        return
        
    if message.from_user:
        await add_user(message.from_user.id)
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ADD ADMIN 
@app.on_message(filters.command("addadmin") & filters.private)
async def add_admin(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")

    if len(message.command) < 2:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ /addadmin user_id")

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("‼️ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ")

    user = await client.get_users(user_id)

    name = user.first_name
    username = user.username if user.username else "None"

    await add_admin_db(user_id, name, username)

    await message.reply_text(f"✅️ ᴀᴅᴍɪɴ ɪs ᴀᴅᴅᴇᴅ : {user_id}")

    # Send message to that user
    try:
        await client.send_message(
            chat_id=user_id,
            text="🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴘʀᴏᴍᴏᴛᴇᴅ ᴛᴏ 𝗔𝗗𝗠𝗜𝗡\n\nYᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs."
        )
    except Exception as e:
        print(f"Fᴀɪʟᴇᴅ Tᴏ Nᴏᴛɪғʏ Aᴅᴍɪɴ : {e}")
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# REMOVE ADMIN 
@app.on_message(filters.command("removeadmin") & filters.private)
async def remove_admin(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")

    if len(message.command) < 2:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ /removeadmin user_id")

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("‼️ ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ")

    await remove_admin_db(user_id)

    await message.reply_text(f"✅️ ᴀᴅᴍɪɴ ɪs ʀᴇᴍᴏᴠᴇᴅ : {user_id}")
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

#ADMIN LIST
@app.on_message(filters.command("adminlist") & filters.private)
async def admin_list(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "🚫 𝗬𝗼𝘂 𝗔𝗿𝗲 𝗡𝗼𝘁 𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝗧𝗼 𝗨𝘀𝗲 𝗧𝗵𝗶𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱"
        )

    admins = await get_all_admins()

    if not admins:
        return await message.reply_text(
            "‼️ Nᴏ Aᴅᴍɪɴs Fᴏᴜɴᴅ Iɴ Lɪsᴛ"
        )

    text = "👑 Aᴅᴍɪɴ Lɪsᴛ\n\n"

    for i, admin in enumerate(admins, start=1):

        name = admin.get("name", "Unknown")
        username = admin.get("username", "None")
        user_id = admin.get("user_id")

        text += (
            f"{i}. 𝗡𝗮𝗺𝗲: {name}\n"
            f"  𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: @{username if username != 'None' else 'no_username'}\n"
            f"  𝗜𝗗: {user_id}\n\n"
        )

    await message.reply_photo(
        photo=ADMINLIST_IMAGE,
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
    
@app.on_message(filters.command("index") & filters.private)
async def index_command(client, message):

    if not (
        message.from_user.id == OWNER_ID
        or await is_admin(message.from_user.id)
    ):
        return await message.reply_text(
            "🚫 **You are not authorized to use this command.**"
        )

    rows = []

    for i in range(0, 26, 4):
        row = []

        for letter in LETTERS[i:i+4]:
            row.append(
                InlineKeyboardButton(
                    letter,
                    callback_data=f"index_{letter}"
                )
            )

        rows.append(row)

    rows.append(
        [
            InlineKeyboardButton(
                "• ᴄʟᴏsᴇ •",
                callback_data="close"
            )
        ]
    )

    await message.reply_photo(
        photo=INDEX_IMAGE,
        caption=(
            " **Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Iɴᴅᴇx**\n\n"
            "**Sᴇʟᴇᴄᴛ ᴀ ʟᴇᴛᴛᴇʀ ᴛᴏ ᴠɪᴇᴡ ᴄʜᴀɴɴᴇʟs.**"
        ),
        reply_markup=InlineKeyboardMarkup(rows)
    )

# ------------------------- #
# INDEX LETTER CALLBACK
# ------------------------- #

@app.on_callback_query(filters.regex(r"^index_([A-Z])$"))
async def index_letter_callback(client, query):

    letter = query.data.split("_")[1]

    channels = await get_force_subs()

    text = f"**ᴄʜᴀɴɴᴇʟs sᴛᴀʀᴛɪɴɢ ᴡɪᴛʜ {letter}**\n\n"

    found = False

    for i, ch in enumerate(channels, start=1):

        try:
            chat = await client.get_chat(ch)

            if not chat.title.upper().startswith(letter):
                continue

            found = True

            if chat.username:
                text += (
                    f"**{i}.** @{chat.username}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )
            else:
                text += (
                    f"**{i}.** {chat.title}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )

        except:
            continue

    if not found:
        text += "**Nᴏ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ ᴏʀ ᴀᴅᴅᴇᴅ**"

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "• ʙᴀᴄᴋ •",
                    callback_data="index_back"
                ),
                InlineKeyboardButton(
                    "• ᴄʟᴏsᴇ •",
                    callback_data="close"
                )
            ]
        ]
    )

    await query.message.edit_caption(
        caption=text,
        reply_markup=keyboard
    )
    
# ------------------------- #
# FORCE SUBSCRIBE COMMANDS
# ------------------------- #

@app.on_message(filters.command("ban") & filters.private)
async def ban(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/ban user_id"
        )

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("Invalid User ID")

    await ban_user(user_id)

    await message.reply_text(
        f"✅ User `{user_id}` has been banned."
    )

    try:
        await client.send_message(
            user_id,
            "**🚫 You have been banned from using this bot.**"
        )
    except:
        pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("unban") & filters.private)
async def unban(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/unban user_id"
        )

    try:
        user_id = int(message.command[1])
    except:
        return await message.reply_text("Invalid User ID")

    await unban_user(user_id)

    await message.reply_text(
        f"✅ User `{user_id}` has been unbanned."
    )

    try:
        await client.send_message(
            user_id,
            "**🎉 You have been unbanned. You can use the bot again.**"
        )
    except:
        pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("banlist") & filters.private)
async def banlist(client, message):

    if message.from_user.id != OWNER_ID:
        return

    users = await get_banned_users()

    if not users:
        return await message.reply_text(
            "✅ No banned users."
        )

    text = "🚫 **Banned Users List**\n\n"

    for i, user in enumerate(users, 1):
        text += f"**{i}.** `{user}`\n"

    await message.reply_photo(
        photo="https://graph.org/file/26cccf142db47cbcc489e-5d5b36c222d0b2d898.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("addfsub") & filters.private)
async def add_fsub(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("🚫 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃...")

    # Reply to forwarded channel post
    if message.reply_to_message:

        reply = message.reply_to_message

        if reply.forward_from_chat:
            chat = reply.forward_from_chat

        elif reply.sender_chat:
            chat = reply.sender_chat

        else:
            return await message.reply_text(
                "‼️ Reply to a forwarded channel post."
            )

        channel = chat.id

        # Username / ID method
    else:

        if len(message.command) < 2:
            return await message.reply_text(
                "Usage:\n"
                 "/addfsub @channel\n"
                 "/addfsub -100xxxxxxxxxx\n\n"
                 "OR reply to a forwarded private channel post with /addfsub."
            )

        channel = message.command[1]

        try:
            channel = int(channel)
        except:
            channel = channel.replace("@", "")

    try:
        chat = await client.get_chat(channel)

        me = await client.get_me()

        member = await client.get_chat_member(chat.id, me.id)

        if member.status not in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            return await message.reply_text(
                "‼️ 𝖥𝗂𝗋𝗌𝗍 𝗆𝖺𝗄𝖾 𝗆𝖾 𝖠𝖽𝗆𝗂𝗇 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅."
            )

    except Exception as e:
        return await message.reply_text(
            f"‼️ 𝖨𝗇𝗏𝖺𝗅𝗂𝖽 𝖢𝗁𝖺𝗇𝗇𝖾𝗅.\n\n{e}"
        )
    channels = await get_force_subs()

    if str(chat.id) in channels:
        return await message.reply_text(
            "⚠️ This channel is already in Force Subscribe."
        )
    
    if chat.username and chat.username in channels:
        return await message.reply_text(
            "⚠️ This channel is already in Force Subscribe."
        )

    await add_force_sub(chat.id)

    await message.reply_text(
        f"**Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Aᴅᴅᴇᴅ**\n\n"
        f"**ᴄʜᴀɴɴᴇʟ:** {chat.title}\n"
        f"*ɪᴅ:** `{chat.id}`"
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("removefsub") & filters.private)
async def remove_fsub(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("🚫 Unauthorized.")

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n"
            "/removefsub @channel\n"
            "/removefsub -100xxxxxxxxxx"
        )

    channel = message.command[1]

    try:
        channel = int(channel)
    except:
        channel = channel.replace("@", "")

    try:
        chat = await client.get_chat(channel)

        await remove_force_sub(chat.id)

        if chat.username:
            await remove_force_sub(chat.username)
            await remove_force_sub(f"@{chat.username}")

        await message.reply_text(
            f"✅ Removed **{chat.title}** from Force Subscribe."
        )

    except Exception as e:
        return await message.reply_text(
            f"❌ Failed to remove.\n\n{e}"
        )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("fsublist") & filters.private)
async def fsub_list(client, message):

    if not (message.from_user.id == OWNER_ID or await is_admin(message.from_user.id)):
        return await message.reply_text("🚫 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃..")

    channels = await get_force_subs()

    if not channels:
        return await message.reply_text(
            "‼️ Nᴏ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Cʜᴀɴɴᴇʟs ᴀᴅᴅᴇᴅ ᴏʀ Nᴏᴛ Fᴏᴜɴᴅ."
        )

    text = "**📢 Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Cʜᴀɴɴᴇʟs Lɪsᴛ**\n\n"

    for i, ch in enumerate(channels, start=1):
        try:
            chat = await client.get_chat(ch)

            if chat.username:
                text += f"**{i}.** @{chat.username}\n"
            else:
                text += (
                    f"**{i}.** {chat.title}\n"
                    f"**ID:** `{chat.id}`\n\n"
                )

        except:
            if str(ch).startswith("-100"):
                text += (
                    f"**{i}.** 🔒 Private Channel\n"
                    f"**ID:** `{ch}`\n\n"
                )
            else:
                text += f"**{i}.** @{ch}\n"

    await message.reply_photo(
        photo="https://graph.org/file/ffdbc01d09855874311b1-5f3f1eae52d984db3d.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")
                ]
            ]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# INDEX BACK CALLBACK
# ------------------------- #

@app.on_callback_query(filters.regex("^index_back$"))
async def index_back_callback(client, query):

    rows = []

    for i in range(0, 26, 4):
        row = []

        for letter in LETTERS[i:i+4]:
            row.append(
                InlineKeyboardButton(
                    letter,
                    callback_data=f"index_{letter}"
                )
            )

        rows.append(row)

    rows.append(
        [
            InlineKeyboardButton(
                "• ᴄʟᴏsᴇ •",
                callback_data="close"
            )
        ]
    )

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=INDEX_IMAGE,
            caption=(
                "**Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Iɴᴅᴇx**\n\n"
                "**Sᴇʟᴇᴄᴛ ᴀ ʟᴇᴛᴛᴇʀ ᴛᴏ ᴠɪᴇᴡ ᴄʜᴀɴɴᴇʟs**."
            )
        ),
        reply_markup=InlineKeyboardMarkup(rows)
    )

# ------------------------- #
# FORCE SUB CALLBACK
# ------------------------- #

    # ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_callback_query(filters.regex("checksub"))
async def checksub_callback(client, query):

    ok, keyboard = await check_force_sub(
        client,
        query.from_user.id
    )

    if not ok:
        return await query.answer(
            "‼️ Jᴏɪɴ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs ғɪʀsᴛ.",
            show_alert=True
        )

    # animation
    await query.message.edit_media(
        InputMediaPhoto(
            CHECKING_IMAGE,
            "Cʜᴇᴄᴋɪɴɢ Sᴜʙsᴄʀɪᴘᴛɪᴏɴ..."
        )
    )

    await asyncio.sleep(1)

    await query.message.edit_caption("!")

    await asyncio.sleep(0.5)

    await query.message.edit_caption("!!")

    await asyncio.sleep(0.5)

    await query.message.edit_caption("!!!")

    await asyncio.sleep(0.5)

    param = await get_verify(query.from_user.id)

    if not param:
        return await query.answer(
            "❌ Verification expired. Go Back Try Again.",
            show_alert=True
        )

    # remove force subscribe message
    await query.message.delete()

    # directly run start
    fake = type("obj", (), {})()

    fake.from_user = query.from_user
    fake.command = ["start", param]
    fake.text = f"/start {param}"
    fake.chat = query.message.chat

    fake.reply_text = query.message.reply_text
    fake.reply_photo = query.message.reply_photo
    fake.reply_video = query.message.reply_video
    fake.reply_audio = query.message.reply_audio
    fake.reply_document = query.message.reply_document
    fake.reply_animation = query.message.reply_animation
    fake.reply_sticker = query.message.reply_sticker
    fake.reply = query.message.reply_text

    await start(client, fake)
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
        
# ABOUT HANDLER
@app.on_callback_query(filters.regex("about"))
async def about_callback(client, query):
    await query.message.edit_text(
        "⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟\n\n"
        "‣ ᴍʏ ɴᴀᴍᴇ : [ᴀᴇʀᴏ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ](https://t.me/Aero_FileStoreBot)\n"
        "‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴍᴏʜᴀᴍᴍᴇᴅ](https://t.me/Mr_Mohammed_29)\n"
        "‣ ʟɪʙʀᴀʀʏ : [ᴘʏʀᴏɢʀᴀᴍ 𝟸.𝟶](https://pypi.org/project/Pyrogram/)\n"
        "‣ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ 𝟹](https://www.python.org/downloads/)\n"
        "‣ ᴅᴀᴛᴀ ʙᴀsᴇ : [ᴍᴏɴɢᴏ ᴅʙ](https://www.mongodb.com/)\n"
        "‣ ʙᴏᴛ sᴇʀᴠᴇʀ : [Bᴏᴛs Sᴇʀᴠᴇʀ](https://render.com)\n"
        "‣ ᴜᴘᴅᴀᴛᴇs : [ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs](https://t.me/Aero_Unity)\n"
        "‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.𝟶 [sᴛᴀʙʟᴇ](https://t.me/Aero_Unity)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="home")]]
        ),
        parse_mode=ParseMode.MARKDOWN
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# HOME HANDLER
@app.on_callback_query(filters.regex("home"))
async def home_callback(client, query):

    photo = random.choice(IMAGES)

    await query.message.edit_media(
        media=InputMediaPhoto(
            media=photo,
            caption=(
                "𝗛𝗲𝗹𝗹𝗼 ♡,\n\n"
                "›› 𝗜 𝗰𝗮𝗻 𝘀𝘁𝗼𝗿𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗦𝗽𝗲𝗰𝗶𝗳𝗶𝗲𝗱 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝗼𝘁𝗵𝗲𝗿 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗮𝗰𝗰𝘀𝘀 𝗶𝘁 𝗳𝗿𝗼𝗺 𝘀𝗽𝗲𝗰𝗶𝗮𝗹 𝗹𝗶𝗻𝗸."
            ),
            parse_mode=ParseMode.MARKDOWN
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/Aero_Unity"),
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/Mr_Mohammed_29")
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_callback_query(filters.regex("^close$"))
async def close_button(client, query):
    await query.message.delete()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# REFRESH STATS 
@app.on_callback_query(filters.regex("refresh_stats"))
async def refresh_stats(client, query):

    start = time.time()
    total = await total_users()

    uptime_seconds = int(time.time() - START_TIME)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    ping = round((time.time() - start) * 1000)

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ", callback_data="refresh_stats")]]
    )

    process = psutil.Process()
    memory = process.memory_info().rss / (1024 * 1024)

    await query.message.edit_text(
        f"📊 **𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀**\n\n"
        f"👥 Usᴇʀs: {total}\n"
        f"⏱ Uᴘᴛɪᴍᴇ: {hours}h {minutes}m {seconds}s\n"
        f"⚡ Pɪɴɢ: {ping} ms\n"
        f"🧠 Mᴇᴍᴏʀʏ Usᴀɢᴇ: {memory:.2f} MB\n"
        f"🧾 Vᴇʀsɪᴏɴ: {BOT_VERSION}",
        reply_markup=keyboard
    )

    await query.answer("Sᴛᴀᴛs Uᴘᴅᴀᴛᴇᴅ 🔄")   

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# ALIVE COMMAND
# ------------------------- #

@app.on_message(filters.command("alive"))
async def alive(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 You are banned from using this bot."
        )

    await message.reply_photo(
        photo="https://graph.org/file/af61bc94f516c210ecb37-7cdb22e66ea9539e3b.jpg",
        caption=(
            "❤️ **Yᴏᴜ ᴀʀᴇ ᴠᴇʀʏ ʟᴜᴄᴋʏ 🤞 I ᴀᴍ ᴀʟɪᴠᴇ ❤️\n\n"
            "Pʀᴇss /start ᴛᴏ ᴜsᴇ ᴍᴇ!**"
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# ID COMMAND
# ------------------------- #

@app.on_message(filters.command("id"))
async def get_id(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 You are banned from using this bot."
        )

    user = message.from_user

    text = (
        "👤 **Usᴇʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ**\n\n"
        f"➲ **Fɪʀsᴛ Nᴀᴍᴇ**: {user.first_name or 'None'}\n"
        f"➲ **Lᴀsᴛ Nᴀᴍᴇ**: {user.last_name or 'None'}\n"
        f"➲ **Usᴇʀɴᴀᴍᴇ**: {user.username or 'None'}\n"
        f"➲ **Tᴇʟᴇɢʀᴀᴍ ID**: {user.id}\n"
        f"➲ **Dᴀᴛᴀ Cᴇɴᴛʀᴇ**: {user.dc_id or 'Unknown'}"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "👤 Vɪᴇᴡ Pʀᴏғɪʟᴇ",
                    url=f"https://t.me/{user.username}" if user.username else f"tg://openmessage?user_id={user.id}"
                )
            ]
        ]
    )

    try:
        photos = await client.get_profile_photos(
            user.id,
            limit=1
        )

        if photos:
            await message.reply_photo(
                photos[0].file_id,
                caption=text,
                reply_markup=keyboard
            )
        else:
            await message.reply_text(
                text,
                reply_markup=keyboard
            )

    except:
        await message.reply_text(
            text,
            reply_markup=keyboard
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("system"))
async def system_info(client, message):

    if await is_banned(message.from_user.id):
        return await message.reply_text(
            "🚫 You are banned from using this bot."
        )

    os_name = platform.system()

    uptime = int(time.time() - START_TIME)
    d, rem = divmod(uptime, 86400)
    h, rem = divmod(rem, 3600)
    m, s = divmod(rem, 60)

    sys_time = int(time.time() - psutil.boot_time())
    sd, rem = divmod(sys_time, 86400)
    sh, rem = divmod(rem, 3600)
    sm, ss = divmod(rem, 60)

    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    text = (
        "💻 **Sʏsᴛᴇᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Pᴀɴᴇʟ**\n\n"
        f"🖥️ **OS Dᴇᴛᴀɪʟs** : {os_name}\n"
        f"⏰ **Bᴏᴛ Uᴘᴛɪᴍᴇ** : {d}ᴅ : {h}ʜ : {m}ᴍ : {s}s\n"
        f"🔄 **Sʏsᴛᴇᴍ Uᴘᴛɪᴍᴇ** : {sd}ᴅ : {sh}ʜ : {sm}ᴍ : {ss}s\n"
        f"💾 **Rᴀᴍ Usᴀɢᴇ** : {ram.used/(1024**3):.2f} GB / {ram.total/(1024**3):.2f} GB\n"
        f"📁 **Dɪsᴋ Usᴀɢᴇ** : {disk.used/(1024**3):.2f} GB / {disk.total/(1024**3):.2f} GB"
    )

    await message.reply_photo(
        photo="https://graph.org/file/3999f429ad9b0b1317f28-7591e7676c147975c9.jpg",
        caption=text
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("restart") & filters.private)
async def restart_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "🚫 <b>You are not authorized to use this command.</b>"
        )

    text = (
        "<blockquote>🔄 <b>BOT RESTART</b></blockquote>\n\n"
        "• <b>Status:</b> Restarting Bot...\n"
        "• <b>Please wait:</b> 5–10 Seconds\n\n"
        "<blockquote>⚡ All services will automatically reconnect after restart.</blockquote>"
    )

    await message.reply_photo(
        photo="https://graph.org/file/14c3a336058422b14549d-85d887f6fd8a9cead5.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]]
        )
    )

    os.execl(sys.executable, sys.executable, *sys.argv)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("clearcache") & filters.private)
async def clear_cache(client, message):

    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "**🚫 You are not authorized to use this command.**"
        )

    # Clear Python garbage
    collected = gc.collect()

    # Clear your custom caches here (if they exist)
    try:
        INDEX_CACHE.clear()
    except:
        pass

    try:
        BATCH_USERS.clear()
    except:
        pass

    text = (
        "<blockquote><b>🗑 CACHE CLEANED SUCCESSFULLY</b></blockquote>\n\n"
        f"🧹 <b>Garbage Objects Collected:</b> <code>{collected}</code>\n"
        "📦 <b>Memory Cache:</b> Cleared ✅\n"
        "⚡ <b>Bot Performance:</b> **Optimized**\n\n"
        "<blockquote>"
        "The temporary cache has been removed.\n"
        "The bot is now running with a fresh cache."
        "</blockquote>"
    )

    await message.reply_photo(
        photo="https://graph.org/file/82399e44509fe3e309f1a-c643c16f816cfb8273.jpg",  # Change to your image
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("fileinfo") & filters.private)
async def fileinfo(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if not message.reply_to_message:
        return await message.reply_text(
            "❌ Reply to a file with <code>/fileinfo</code>"
        )

    media = (
        message.reply_to_message.document
        or message.reply_to_message.video
        or message.reply_to_message.audio
        or message.reply_to_message.photo
        or message.reply_to_message.animation
        or message.reply_to_message.voice
        or message.reply_to_message.video_note
    )

    if not media:
        return await message.reply_text(
            "❌ Reply to a valid media file."
        )

    size = media.file_size or 0

    if size >= 1024**3:
        size_text = f"{size/(1024**3):.2f} GB"
    else:
        size_text = f"{size/(1024**2):.2f} MB"

    caption = message.reply_to_message.caption or "No Caption"

    text = f"""
<blockquote><b>📄 FILE INFORMATION</b></blockquote>

📁 <b>File Name</b> <code>{getattr(media, 'file_name', 'Unknown')}</code>
📦 <b>File Size</b> <code>{size_text}</code>
🏷 <b>File Type</b> <code>{media.__class__.__name__}</code>

🆔 <b>File ID</b> <code>{media.file_id}</code>

🔑 <b>Unique ID</b> <code>{media.file_unique_id}</code>

👤 <b>Uploader ID</b> <code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Unknown'}</code>
📝 <b>Caption</b> <code>{caption}</code>
<blockquote>
✅ File information retrieved successfully.
</blockquote>
"""

    await message.reply_photo(
        photo="https://graph.org/file/8823f724144e44ba40b4f-a6a7bc3ab6bcbe6912.jpg",  # Replace with your image
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

PRIVACY_TEXT = """
<blockquote><b>🔒 PRIVACY POLICY</b></blockquote>

Your privacy is important to us.

<b>📂 Data We Store</b>
• Telegram User ID
• Uploaded File IDs
• File Names & Captions
• Force Subscribe Status
• Download Statistics

<b>❌ Data We Never Store</b>
• Passwords
• Phone Numbers
• Private Chats
• Payment Information

<b>🔐 Security</b>
All data is stored securely inside the bot database and is never shared with third parties.
"""

@app.on_message(filters.command("privacy") & filters.private)
async def privacy_command(client, message):

    await message.reply_photo(
        photo="https://graph.org/file/aa75d86b96cc9de2febbb-8100e96d3a0dfcc88b.jpg",
        caption=PRIVACY_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    
@app.on_message(filters.command("version") & filters.private)
async def version_cmd(client, message):

    caption = f"""
<blockquote><b>🚀 BOT VERSION INFORMATION</b></blockquote>

🤖 <b>Bot Version</b> <code>{BOT_VERSION}</code>
🐍 <b>Python</b> <code>3.11.15</code>
⚡ <b>Pyrogram</b> <code>2.0.106</code>
🗄 <b>Database</b> <code>MongoDB Atlas</code>
🌐 <b>Hosting</b> <code>Render Web Service</code>
👨‍💻 <b>Developer</b> <a href="https://t.me/Mr_Mohammed_29">Mohammed</a>
📢 <b>Updates Channel</b> <a href="https://t.me/Aero_Unity">Aero Unity</a>
💬 <b>Support Group</b> <a href="https://t.me/+KWvhNb8kkmExNDc1">Discussion</a>
🌟 <b>GitHub</b> <a href="https://github.com/MohammedDev-yt">Mohammed Dev</a>

<blockquote>
✅ Running the latest premium build with enhanced performance and stability.
</blockquote>
"""

    await message.reply_photo(
        photo="https://graph.org/file/c658f88f509dd0c786ac5-44bdf2692f1ca00b29.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("support") & filters.private)
async def support_cmd(client, message):

    caption = """
<blockquote><b>🛠 SUPPORT CENTER</b></blockquote>

• Bot Issues
• Database Problems
• Force Subscribe Help
• Deployment Support
• Feature Requests
• Bug Reports

<blockquote>
📨 Response time is usually within a few hours.
Please describe your issue clearly when asking for help.
</blockquote>
"""

    await message.reply_photo(
        photo="https://graph.org/file/ffdbc01d09855874311b1-5f3f1eae52d984db3d.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •",
                        url="https://t.me/Mr_Mohammed_29"
                    ),
                    InlineKeyboardButton(
                        "• Support •",
                        url="https://t.me/+KWvhNb8kkmExNDc1"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴜᴘᴅᴀᴛᴇs •",
                        url="https://t.me/Aero_Unity"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("storage") & filters.private)
async def storage_cmd(client, message):

    storage = await storage_used()
    total = await total_files()

    kb = storage / 1024
    mb = storage / (1024 ** 2)
    gb = storage / (1024 ** 3)
    tb = storage / (1024 ** 4)

    caption = f"""
<blockquote><b>💾 STORAGE INFORMATION</b></blockquote>

📂 <b>Total Files :</b> <code>{total:,}</code>
💽 <b>Bytes :</b> <code>{storage:,} B</code>
📀 <b>Kilobytes :</b> <code>{kb:.2f} KB</code>
📦 <b>Megabytes :</b> <code>{mb:.2f} MB</code>
🗄 <b>Gigabytes :</b> <code>{gb:.2f} GB</code>
☁️ <b>Terabytes :</b> <code>{tb:.4f} TB</code>
<blockquote>
✅ Database Storage Calculated Successfully
</blockquote>
"""

    await message.reply_photo(
        photo="https://graph.org/file/61d73191fab95f9beab61-3e43b0219ea4150b8c.jpg",  # Replace with your image
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("backupdb") & filters.private)
async def backup_database(client, message):

    if message.from_user.id != OWNER_ID:
        return

    msg = await message.reply_photo(
        photo="https://graph.org/file/f66be4faa4d6b5532dec4-63ae8e6c8ba2f306e3.jpg",  # Backup Image
        caption="""
<blockquote>💾 <b>DATABASE BACKUP</b></blockquote>

⏳ <b>Creating database backup...</b>
""",
    )

    try:

        backup_file = await export_database("database_backup.json")

        await message.reply_document(
            document=backup_file,
            file_name="@Aero_Unity_Database_Backup.json",
            caption=f"""
<blockquote>✅ <b>DATABASE BACKUP COMPLETED</b></blockquote>
📂 <b>Backup File :</b> <code>AU_Database_Backup.json</code>
🗃 <b>Status :</b> Successfully Exported
⚠️ <b>This backup contains all MongoDB collections only.</b>
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

        await msg.delete()

    except Exception as e:

        await msg.edit_caption(
            f"""
<blockquote>❌ <b>BACKUP FAILED</b></blockquote><code>{e}</code>
"""
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("restoredb") & filters.private)
async def restore_database_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply_photo(
            photo="https://graph.org/file/f66be4faa4d6b5532dec4-63ae8e6c8ba2f306e3.jpg",
            caption=(
                "<blockquote>♻️ <b>Database Restore</b></blockquote>\n\n"
                "Reply to a <code>backup.json</code> file with:\n\n"
                "<code>/restoredb</code>"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]
            ])
        )

    status = await message.reply_photo(
        photo=ADMIN_IMAGE,
        caption=(
            "<blockquote>⏳ Restoring Database...</blockquote>\n\n"
            "Please wait..."
        )
    )

    file_path = await message.reply_to_message.download()

    try:
        success = await import_database(file_path)

        if success:
            await status.edit_caption(
                caption=(
                    "<blockquote>✅ Database Restored Successfully</blockquote>\n\n"
                    "All collections have been restored from the uploaded backup."
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]
                ])
            )
        else:
            await status.edit_caption(
                caption=(
                    "<blockquote>❌ Restore Failed</blockquote>\n\n"
                    "Invalid or corrupted backup file."
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]
                ])
            )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("cleanup") & filters.private)
async def cleanup_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    status = await message.reply_photo(
        photo="https://graph.org/file/85aeb98b0b394a2a29759-367cf355206fa8ef47.jpg",
        caption="""
<blockquote><b>🧹 SYSTEM CLEANUP</b></blockquote>

⏳ Cleaning temporary data...
• Please Wait a sec.....
"""
    )

    verify_deleted = 0
    temp_deleted = 0

    # Clear Verify Cache
    result = await verify_db.delete_many({})
    verify_deleted = result.deleted_count

    # Remove temp folders/files
    temp_dirs = [
        "downloads",
        "temp",
        "cache"
    ]

    for folder in temp_dirs:

        if os.path.exists(folder):

            for file in os.listdir(folder):

                path = os.path.join(folder, file)

                try:

                    if os.path.isfile(path):
                        os.remove(path)
                        temp_deleted += 1

                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                        temp_deleted += 1

                except:
                    pass

    await status.edit_caption(
        caption=f"""
<blockquote><b>✅ CLEANUP COMPLETED</b></blockquote>

🧹 <b>Verify Cache Cleared</b> : <code>{verify_deleted}</code>
🗂 <b>Temporary Files Removed</b> : <code>{temp_deleted}</code>
💾 <b>Database Files</b> : <code>Safe</code>
👥 <b>Users</b> : <code>Safe</code>
📂 <b>Stored Files</b> : <code>Safe</code>
<blockquote>
System cleanup completed successfully.
</blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("analysis") & filters.private)
async def analysis_cmd(client, message):

    users = await total_users()
    files = await total_files()
    admins = await total_admins()
    today = await today_files()
    week = await week_files()
    storage = await storage_used()

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    uptime = int(time.time() - START_TIME)

    h = uptime // 3600
    m = (uptime % 3600) // 60
    s = uptime % 60

    text = f"""
<blockquote><b>📊 BOT ANALYSIS REPORT</b></blockquote>

<b>👥 Users :</b> <code>{users:,}</code>
<b>📂 Files :</b> <code>{files:,}</code>
<b>👮 Admins :</b> <code>{admins}</code>
<b>📅 Today's Uploads :</b> <code>{today}</code>
<b>🗓 This Week :</b> <code>{week}</code>
<b>💾 Stored Data :</b> <code>{format_size(storage)}</code>
<b>⚙ CPU Usage :</b> <code>{cpu}%</code>
<b>🧠 RAM :</b> <code>{format_size(ram.used)} / {format_size(ram.total)}</code>
<b>💽 Disk :</b> <code>{format_size(disk.used)} / {format_size(disk.total)}</code>
<b>🐍 Python :</b> <code>{platform.python_version()}</code>
<b>🤖 Pyrogram :</b> <code>2.0.106</code>
<b>🖥 Platform :</b> <code>{platform.system()} {platform.release()}</code>
<b>⏳ Uptime :</b> <code>{h}h {m}m {s}s</code>
<b>Status :</b> ✅ Healthy
"""

    await message.reply_photo(
        photo="https://graph.org/file/acd6215d3f851eb72a772-4a988e1a662a3c1693.jpg",
        caption=text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("speedtest") & filters.private)
async def speedtest_cmd(client, message):

    msg = await message.reply_text(
        "⚡ Running internet speed test...\n"
        "This may take a 10-20 sec..."
    )

    try:
        start = time.time()

        st = speedtest.Speedtest()

        st.get_best_server()

        download = st.download() / 1024 / 1024
        upload = st.upload() / 1024 / 1024

        ping = st.results.ping

        elapsed = round(time.time() - start, 2)

        await msg.delete()

        caption = f"""
<blockquote><b>⚡ SPEED TEST RESULT</b></blockquote>

📡 <b>Server :</b> <code>{st.results.server['sponsor']}</code>
🌍 <b>Country :</b> <code>{st.results.server['country']}</code>
📥 <b>Download :</b> <code>{download:.2f} Mbps</code>
📤 <b>Upload :</b> <code>{upload:.2f} Mbps</code>
📶 <b>Ping :</b> <code>{ping:.2f} ms</code>
⏱ <b>Time Taken :</b> <code>{elapsed} sec</code>

• <b>Network Speed Test Completed.</b>
"""

        await message.reply_photo(
            photo="https://graph.org/file/24b1d71722e3272349f71-dc01805818fa2e8c67.jpg",
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• ᴄʟᴏsᴇ •",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    except Exception as e:
        await msg.edit(
            f"❌ Speed test failed.\n\n<code>{e}</code>"
        )
        
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("filestats") & filters.private)
async def file_stats_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    total_files = await files.count_documents({})

    videos = await files.count_documents(
        {"file_type": "video"}
    )

    documents = await files.count_documents(
        {"file_type": "document"}
    )

    audios = await files.count_documents(
        {"file_type": "audio"}
    )

    photos = await files.count_documents(
        {"file_type": "photo"}
    )

    others = total_files - (
        videos +
        documents +
        audios +
        photos
    )

    total_size = 0
    total_downloads = 0

    async for file in files.find(
        {},
        {
            "file_size": 1,
            "download_count": 1
        }
    ):
        total_size += file.get("file_size", 0)
        total_downloads += file.get("download_count", 0)

    gb = total_size / (1024 ** 3)

    caption = f"""
<blockquote><b>📂 FILE STATISTICS</b></blockquote>

📦 <b>Total Files</b> : <code>{total_files:,}</code>
🎬 <b>Videos</b> : <code>{videos:,}</code>
📄 <b>Documents</b> : <code>{documents:,}</code>
🎵 <b>Audios</b> : <code>{audios:,}</code>
🖼 <b>Photos</b> : <code>{photos:,}</code>
📁 <b>Others</b> : <code>{others:,}</code>
💾 <b>Total Storage</b> : <code>{gb:.2f} GB</code>
📥 <b>Total Downloads</b> : <code>{total_downloads:,}</code>
<b>Status :</b> <code>Healthy ✅</code>
"""

    await message.reply_photo(
        photo="https://graph.org/file/76121727251931b1c5ef0-2f318b71367ab9951f.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •",
                        callback_data="close"
                    )
                ]
            ]
        )
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@app.on_message(filters.command("dbinfo"))
async def dbinfo_cmd(client, message):
    
    if message.from_user.id != OWNER_ID:
        return await message.reply_text(
            "> ❌ You are not authorized to use this command."
        )

    total_files = await files.count_documents({})
    total_users = await users.count_documents({})

    await message.reply_text(
        f"> **🗄 Database Info**\n\n"
        f"> **📁 Total Files : `{total_files}`**\n"
        f"> **🔗 Database : [MongoDB](https://www.mongodb.com/) ✅**\n"
        f"> **🤖 Bot : [File Store Bot](https://t.me/{client.me.username})**",
        disable_web_page_preview=True,
        quote=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

if __name__ == "__main__":
    keep_alive()  
    print("""
╔══════════════════════════════╗
║   ᴍᴏʜᴀᴍᴍᴇᴅᴅᴇᴠ-ʏᴛ                   ║
║   ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ.            ║
╚══════════════════════════════╝
""")
    app.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #