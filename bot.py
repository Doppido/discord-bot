import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
TARGET_USER_ID = 474609920419823616  # replace with the person's ID
AUDIO_FILE = r"C:\Users\Lauri\Desktop\programovanie\dc\Havah Nagilah final.wav"

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # Check if the target user joined a voice channel
    if member.id == TARGET_USER_ID:
        if before.channel is None and after.channel is not None:
            channel = after.channel

            vc = await channel.connect()

            vc.play(discord.FFmpegPCMAudio(AUDIO_FILE))

            while vc.is_playing():
                await discord.utils.sleep_until(discord.utils.utcnow())

            await vc.disconnect()

bot.run(TOKEN)
