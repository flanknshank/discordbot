from discord.ext import commands
import discord
import stageinfo
import image_manipulation
import os

def setup(bot):
    @bot.command()
    async def link(ctx):
        await ctx.send("I love bullying Koroks")

    @bot.command()
    async def jay(ctx):
        await ctx.send("He loves feeding")

    @bot.command()
    async def turf(ctx):
        await ctx.send(stageinfo.get_turf())

    @bot.command()
    async def open(ctx):
        await ctx.send(stageinfo.get_anarchyOpen())

    @bot.command()
    async def series(ctx):
        await ctx.send(stageinfo.get_anarchySeries())

    @bot.command()
    async def image(ctx, arg1, arg2):
        image_map = image_manipulation.make_graphic(arg1,arg2)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def embed(ctx):
        embed=discord.Embed(title="Turf rotation", description="This is an embed that will show how to build an embed and the different components", color=0x90EE90)
        embed.set_thumbnail(url='https://splatoon3.ink/assets/regular.64299513.svg')
        await ctx.send(embed=embed)