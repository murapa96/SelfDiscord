'''
Discord self bot.

This is a self bot, which means it is a bot that runs on your account.
This is against Discord's ToS, and can get your account banned at any time.

This bot is for educational purposes only.

This bot gets a message from a channel, and sends it to a user.
Then, it send the response to the channel.

'''
import discord
from discord.ext.commands import Bot

# Bot settings
BOT_PREFIX = ("?", "!")
TOKEN = "YOUR TOKEN HERE"
USER_ID = "THE USER ID YOU WANT TO SEND THE MESSAGE TO"
CHANNEL_ID = "THE CHANNEL ID YOU WANT TO SEND THE MESSAGE TO"
# Bot client

client = Bot(command_prefix=BOT_PREFIX)

# Bot events

@client.event
async def on_ready():
    print("Bot is ready.")

# Bot commands

@client.command()
async def send_from_channel_to_user(message):
    '''Sends a message from a channel to a user.'''
    channel = client.get_channel(CHANNEL_ID)
    message = await channel.get_message(message)
    await client.send_message(discord.Object(id=USER_ID), message.content)

@client.command()
async def send_from_user_to_channel(*, message):
    '''Sends a message from a given user to a given channel.'''
    channel = client.get_channel(CHANNEL_ID)
    await client.send_message(channel, message)


# Run the bot with the token
client.run(TOKEN, bot=False)

