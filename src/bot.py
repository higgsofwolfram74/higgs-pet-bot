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
        

    @commands.command(name="cat")
    async def cat(self, ctx, breed: str):
        cat = Pet_Pics(Path("./env-var/env.json"), "cat")
        if len(breed) == 4:
            cat.breed_response(breed)

        url = await cat.pet_get()
        await ctx.send(url)

    @commands.command(name="dog")
    async def dog(self, ctx, breed: int):
        dog = Pet_Pics(Path("./env-var/env.json"), "dog")
        if breed > 0 and breed < 264:
            dog.breed_response(str(breed))
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

    @commands.command(name="cat-breed")
    async def cat_breed(self, ctx, breed: str):
        cat_breeds = await Pet_Pics.get_breeds("cat")
        breeds = {breed[1].lower(): breed[0] for breed in cat_breeds}
        if breed in breeds:
            await ctx.send(f"The breed {breed} has the id {breeds[breed]}.")

    @commands.command(name="dog-breed")
    async def dog_breed(self, ctx, breed: str):
        cat_breeds = await Pet_Pics.get_breeds("dog")
        breeds = {breed[1].lower(): breed[0] for breed in cat_breeds}
        if breed.lower() in breeds:
            await ctx.send(f"The breed {breed} has the id {breeds[breed]}.")


bot.add_cog(PetGetter(bot))

bot.run(TOKEN)