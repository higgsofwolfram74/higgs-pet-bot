from pathlib import Path
import json
import discord
from discord.ext import commands

from catcaller import Pet_Pics

TOKEN = json.load(Path("./env-var/env.json").open("r"))["DISCORD_TOKEN"]

bot = commands.Bot(command_prefix="~")


#cog command uses function name as command name
class PetGetter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Howdy")

    @commands.command(name="cat")
    async def cat(self, ctx, *args):
        cat = Pet_Pics(Path("./env-var/env.json"), "cat")
        url = await cat.simple_pet()
        await ctx.send(url)

    @commands.command(name="dog")
    async def dog(self, ctx, *args):
        dog = Pet_Pics(Path("./env-var/env.json"), "dog")
        url = await dog.simple_pet()
        await ctx.send(url)

bot.add_cog(PetGetter(bot))

bot.run(TOKEN)