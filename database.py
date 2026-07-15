# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
from datetime import datetime

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

client = AsyncIOMotorClient(MONGO_URI)
db = client.filebot

files = db.files
users = db.users
admins = db["admins"]
forcesubs = db["forcesubs"]
banned = db["banned"]

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# FILES
async def save_file(file_id, file_unique_id, file_type, caption, thumb=None):
    await files.update_one(
        {"file_unique_id": file_unique_id},
        {"$set": {
            "file_id": file_id,
            "file_unique_id": file_unique_id,
            "file_type": file_type,
            "caption": caption,
            "thumb": thumb
        }},
        upsert=True
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_file(file_unique_id):
    return await files.find_one({"file_unique_id": file_unique_id})
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# USERS
async def add_user(user_id):
    if not user_id:
        return

    await users.update_one(
        {"user_id": int(user_id)},
        {"$setOnInsert": {"user_id": int(user_id)}},
        upsert=True
    )
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_all_users():
    return [u["user_id"] async for u in users.find({}, {"user_id": 1, "_id": 0})]
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def total_users():
    return await users.count_documents({})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ADMIN SYSTEM

async def add_admin_db(user_id, name, username):

    user_id = int(user_id)

    await admins.update_one(
        {"user_id": user_id},
        {"$set": {
            "user_id": user_id,
            "name": name,
            "username": username,
            "joined_date": datetime.utcnow()
        }},
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_all_admins():
    admins_list = []
    async for admin in admins.find({}, {"_id": 0}):
        admins_list.append(admin)
    return admins_list
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def remove_admin_db(user_id):
    await admins.delete_one({"user_id": int(user_id)})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def is_admin(user_id):
    return await admins.find_one({"user_id": int(user_id)}) is not None
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def add_force_sub(channel):

    await forcesubs.update_one(
        {"channel": str(channel)},
        {"$set": {"channel": str(channel)}},
        upsert=True
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def remove_force_sub(channel):

    await forcesubs.delete_one(
        {"channel": str(channel)}
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_force_subs():

    channels = []

    async for ch in forcesubs.find({}, {"_id": 0}):
        channels.append(ch["channel"])

    return channels
    
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

verify_db = db.verify_cache


async def save_verify(user_id, param):
    await verify_db.update_one(
        {"user_id": user_id},
        {"$set": {"param": param}},
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_verify(user_id):
    data = await verify_db.find_one({"user_id": user_id})
    if data:
        return data.get("param")
    return None

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def delete_verify(user_id):
    await verify_db.delete_one({"user_id": user_id})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ------------------------- #
# BAN SYSTEM
# ------------------------- #

async def ban_user(user_id):
    await banned.update_one(
        {"user_id": int(user_id)},
        {"$set": {"user_id": int(user_id)}},
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def unban_user(user_id):
    await banned.delete_one({"user_id": int(user_id)})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def is_banned(user_id):
    return await banned.find_one({"user_id": int(user_id)}) is not None

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_banned_users():
    users = []
    async for user in banned.find({}, {"_id": 0}):
        users.append(user["user_id"])
    return users

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #