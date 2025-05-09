# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/idkhelpmeout'):
        # Replace "Strider" with the username you want to search for
        user = get_user("Strider", message.guild)
        if user:
            await message.channel.send(f'{user.mention} how you doin?')
        else:
            await message.channel.send("User not found.")

def get_user(username, guild):
    # Search for the user in the guild's members
    return discord.utils.find(lambda u: u.name == username or u.global_name == username, guild.members)

client.run(os.getenv("BOT_TOKEN"))
