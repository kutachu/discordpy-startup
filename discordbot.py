import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == "＠ジャンプ" or message.content == "@ジャンプ"
        voice = await message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio('jump.mp3'), after=lambda e: print('done', e))
        return

client.run(token)