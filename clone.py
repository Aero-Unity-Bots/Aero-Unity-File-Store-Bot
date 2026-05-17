from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH

CLONES = {}

async def start_clone(user_id, bot_token):

    if user_id in CLONES:
        raise Exception("Clone already running")

    clone = Client(
        session_name=f"sessions/{user_id}",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=bot_token,
        plugins=dict(root="plugins")
    )

    await clone.start()

    me = await clone.get_me()

    CLONES[user_id] = clone

    print(f"Clone Started @{me.username}")

    return me.username


async def stop_clone(user_id):

    clone = CLONES.get(user_id)

    if not clone:
        return

    await clone.stop()

    del CLONES[user_id]
