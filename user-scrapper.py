"""
User scrapper:

 - Gets the list of all users in all the guilds that the current user belongs to using discord.py-self.
"""

import asyncio
import discord
from discord.ext.commands import Bot
import json

# Bot settings
BOT_PREFIX = ("?", "!")
TOKEN = "YOUR TOKEN HERE"

# Bot client
client = Bot(command_prefix=BOT_PREFIX)

# User list

user_list = []

# Bot events

@client.event
async def on_ready():
    print("Bot is ready.")
    await getUsers()

async def getUsers():
    for guild in client.guilds:
        for member in guild.members:
            if member not in user_list:
                user_list.append(client.get_user(member.id))


    print(user_list)


# Run the bot with the token
client.run(TOKEN)



