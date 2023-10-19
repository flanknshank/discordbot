from discord.ext import commands
import discord
import stageinfo
import image_manipulation
import os

def setup(bot):
    @bot.command()
    async def riki(ctx):
        await ctx.send("squeeze")

    @bot.command()
    async def testing(ctx):
        await ctx.send("testing")

    @bot.command()
    async def turf(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_turf()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')


    @bot.command()
    async def open(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchyOpen()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')

    @bot.command()
    async def series(ctx):
        rotation = stageinfo.rotation_info()
        rotation.get_anarchySeries()
        image_map = image_manipulation.make_graphic(rotation.stage1,rotation.stage2,rotation.mode,rotation.time)
        await ctx.send(file=discord.File(image_map))
        os.remove('final.png')


    @bot.command()
    async def embed(ctx):
        embed=discord.Embed(title="Turf rotation", description="This is an embed that will show how to build an embed and the different components", color=0x90EE90)
        embed.set_thumbnail(url='https://splatoon3.ink/assets/regular.64299513.svg')
        await ctx.send(embed=embed)