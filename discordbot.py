import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.author.bot:
        return

    voice = await client.join_voice_channel(client.get_channel("389799900251947012"))
    if message.content == ("＠ジャンプ"):
        player = voice.create_ffmpeg_player('jump.mp3')
        player.start()

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)