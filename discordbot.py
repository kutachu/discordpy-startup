import discord
from discord.voice_client import VoiceClient

import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

voice = None

@client.event
async def on_message(message):
    global voice
    
    if message.author.bot:
        return
    
    if message.content == "＠ジャンプ" or message.content == "@ジャンプ"
        voice = await message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('jump.mp3'), after=lambda e: print('done', e))
        return

client.run(token)