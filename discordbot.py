import discord
import os

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    voice = await client.join_voice_channel(client.get_channel("389799900251947012"))

    if message.content == ("＠jump") or message.content == ("@jump"):
        player = voice.create_ffmpeg_player('jump.mp3')
        player.start()
    
client.run(token)