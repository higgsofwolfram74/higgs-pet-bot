from pathlib import Path
import json
import discord
from discord.ext import commands

TOKEN = json.load(Path("D:/vscode/pyspls/cat-bot/env-var/env.json").open("r"))["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="~")

#cog command uses function name as command name
class PetGetter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Howdy")

bot.add_cog(PetGetter(bot))

bot.run(TOKEN)