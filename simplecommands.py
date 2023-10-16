from discord.ext import commands
import discord
import stageinfo

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
    async def image(ctx):
        with open('wiper.png', 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'new_filename.png'))

    @bot.command()
    async def embed(ctx):
        embed=discord.Embed(title="Turf rotation", description="This is an embed that will show how to build an embed and the different components", color=0x90EE90)
        embed.set_thumbnail(url='https://splatoon3.ink/assets/regular.64299513.svg')
        await ctx.send(embed=embed)