# bot.py
import os
import discord

import config

client = discord.Client()

muted = False
guild = None

@client.event
async def on_ready():
    global guild
    guild = next(g for g in client.guilds if g.name==config.GUILD_NAME)
    print('Connected!')

@client.event
async def on_message(message):
    global muted
    global guild

    if message.content == '!mute' and message.channel.name==config.TEXT_CHANNEL:
        gamers = next(c for c in guild.voice_channels if c.name==config.VOICE_CHANNEL)
        if muted:
            for member in gamers.members:
                await member.edit(mute = False)
            muted = False
        else:
            for member in gamers.members:
                await member.edit(mute = True)
            muted = True

client.run(config.TOKEN)
