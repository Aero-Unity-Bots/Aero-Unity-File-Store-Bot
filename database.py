# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import DESCENDING
from config import MONGO_URI
from datetime import datetime
import json
import os
import time

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
async def save_file(
    file_id,
    file_unique_id,
    file_type,
    caption="",
    thumb=None,
    file_name="",
    file_size=0,
    uploader_id=0
):

    data = {
        "file_id": file_id,
        "file_unique_id": file_unique_id,
        "file_type": file_type,
        "caption": caption,
        "thumb": thumb,
        "file_name": file_name,
        "file_size": file_size,
        "uploader_id": uploader_id,
        "upload_time": int(time.time()),
        "download_count": 0
    }

    await files.update_one(
        {"file_unique_id": file_unique_id},
        {"$set": data},
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

async def total_admins():
    return await admins.count_documents({})
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

    await forcesubs.delete_many(
        {
            "channel": {
                "$in": [
                    str(channel),
                    str(channel).replace("@", "")
                ]
            }
        }
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

# ------------------------- #
# FILE MANAGEMENT
# ------------------------- #

async def get_file_by_unique_id(file_unique_id):
    return await files.find_one(
        {"file_unique_id": file_unique_id}
    )

async def total_files():
    return await files.count_documents({})

# ------------------------- #
# DOWNLOAD COUNT
# ------------------------- #

async def increase_download(file_unique_id):

    await files.update_one(
        {"file_unique_id": file_unique_id},
        {
            "$inc": {
                "download_count": 1
            }
        }
    )


# ------------------------- #
# TODAY FILES
# ------------------------- #

async def today_files():

    now = int(time.time())

    start = now - 86400

    return await files.count_documents(
        {
            "upload_time": {
                "$gte": start
            }
        }
    )


# ------------------------- #
# WEEK FILES
# ------------------------- #

async def week_files():

    now = int(time.time())

    start = now - (7 * 86400)

    return await files.count_documents(
        {
            "upload_time": {
                "$gte": start
            }
        }
    )


# ------------------------- #
# STORAGE
# ------------------------- #

async def storage_used():

    total = 0

    async for file in files.find():

        total += file.get("file_size", 0)

    return total


# ------------------------- #
# TOP USERS
# ------------------------- #

async def top_uploaders(limit=10):

    pipeline = [

        {
            "$group": {
                "_id": "$uploader_id",
                "uploads": {
                    "$sum": 1
                }
            }
        },

        {
            "$sort": {
                "uploads": -1
            }
        },

        {
            "$limit": limit
        }

    ]

    return await files.aggregate(
        pipeline
    ).to_list(length=limit)

# ------------------------- #
# DATABASE BACKUP
# ------------------------- #

COLLECTIONS = {
    "files": files,
    "users": users,
    "admins": admins,
    "forcesubs": forcesubs,
    "verify_cache": verify_db,
    "banned": banned
}


async def export_database(filepath="backup.json"):

    backup = {}

    for name, collection in COLLECTIONS.items():

        backup[name] = []

        async for document in collection.find():

            document["_id"] = str(document["_id"])

            backup[name].append(document)

    with open(filepath, "w", encoding="utf-8") as f:

        json.dump(
            backup,
            f,
            indent=4,
            ensure_ascii=False
        )

    return filepath


# ------------------------- #
# DATABASE RESTORE
# ------------------------- #

async def import_database(filepath):

    if not os.path.exists(filepath):
        return False

    with open(filepath, "r", encoding="utf-8") as f:

        backup = json.load(f)

    for name, collection in COLLECTIONS.items():

        await collection.delete_many({})

        if name not in backup:
            continue

        docs = backup[name]

        for doc in docs:

            doc.pop("_id", None)

        if docs:

            await collection.insert_many(docs)

    return True


# ------------------------- #
# DATABASE INFORMATION
# ------------------------- #

async def database_info():

    info = {}

    for name, collection in COLLECTIONS.items():

        info[name] = await collection.count_documents({})

    return info