'''
Discord self bot.

This is a self bot, which means it is a bot that runs on your account.
This is against Discord's ToS, and can get your account banned at any time.

This bot is for educational purposes only.

This bot gets a message from a channel, and sends it to a user.
Then, it send the response to the channel.

'''
import asyncio
import discord
from discord.ext.commands import Bot

# Bot settings
BOT_PREFIX = ("?", "!")
TOKEN = "YOUR TOKEN HERE"
USER_ID = 0
CHANNEL_ID = 0
IMAGE_CHANNEL_ID = 0
# Bot client

client = Bot(command_prefix=BOT_PREFIX)

# Message Queue

message_queue = []

# USER_ID SlashCommands.
# This is a list of slash commands that the USER_ID has available.

#Subscribe to message queue, each time a message is added to the queue, wait 10 seconds and send it to the USER_ID
async def sendMessages():
    while True:
        if len(message_queue) > 0:
            message = message_queue.pop(0)
            async for command in client.get_channel(IMAGE_CHANNEL_ID).slash_commands():
                print(command.options)
                if command.name == "imagine":
                    await command(prompt=message)
        await asyncio.sleep(10)
# Bot events

@client.event
async def on_ready():
    print("Bot is ready.")
    await sendMessages()

# Bot listeners.

'''
Listen for messages received in CHANNEL_ID and send them to USER_ID and vice versa.
'''
@client.event
async def on_message(message):
    print(message.channel.id == CHANNEL_ID)
    if message.channel.id == CHANNEL_ID:
            # Get the user Bot with the USER_ID available slash_commands
            message_queue.append(message.content)

# Run the bot with the token
client.run(TOKEN)

