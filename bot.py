import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 🧠 Replace with your actual info
OWNER_ID = 774212425603743804  # your Discord user ID
CHANNEL_ID = 1427951571328700497  # the channel ID where message will appear

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_presence_update(before, after):
    if after.id == OWNER_ID:
        # When owner goes ONLINE
        if str(after.status) == "online" and str(before.status) != "online":
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                msg = await channel.send("👑 **The Server Owner is now ONLINE!** 🔥")
                await asyncio.sleep(60)  # wait 1 minute
                await msg.delete()

        # When owner goes OFFLINE
        elif str(after.status) == "offline" and str(before.status) != "offline":
            channel = bot.get_channel(CHANNEL_ID)
            if channel:
                msg = await channel.send("😴 **The Server Owner went OFFLINE.** 💤")
                await asyncio.sleep(60)  # wait 1 minute
                await msg.delete()

import os

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)