from pathlib import Path
import discord

with Path("env-var/bot.env").open('r') as f:
    TOKEN = f.readline().strip("\"")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)