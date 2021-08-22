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
        url = await cat.pet_get()
        await ctx.send(url)

    @commands.command(name="dog")
    async def dog(self, ctx, *args):
        dog = Pet_Pics(Path("./env-var/env.json"), "dog")
        url = await dog.pet_get()
        await ctx.send(url)

    @commands.command(name="cat-gif")
    async def cat_gif(self, ctx):
        cat = Pet_Pics(Path("./env-var/env.json"), "cat")
        cat.query_type(gif = True)
        url = await cat.pet_get()
        await ctx.send(url)
    
    @commands.command(name="dog-gif")
    async def dog_gif(self, ctx):
        dog = Pet_Pics(Path("./env-var/env.json"), "dog")
        dog.query_type(gif = True)
        url = await dog.pet_get()
        await ctx.send(url)

bot.add_cog(PetGetter(bot))

bot.run(TOKEN)