import discord
import os

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
voice_id = os.environ['VOICE_CHANNEL_ID']

@client.event
async def on_message(message):
    if message.author.bot:
        return

    voice = await client.join_voice_channel(message.author.voice_channel)
    if message.content == "＠ジャンプ":
        player = voice.create_ffmpeg_player('./jump.mp3')
        player.start()

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)