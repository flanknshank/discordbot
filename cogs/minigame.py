import asyncio
import discord
from discord.ext import commands
from cogs import moves








def editor(new_embed, value1,value2,player1,player2):
    move1, damage1 = moves.select_move(player1)
    move2, damage2 = moves.select_move(player2)
    value1 = value1 - damage2
    value2 = value2 - damage1
    if value1 <= 0 or value2 <= 0:
        if value1 > value2:
            winner = player1
        else:
            winner = player2
        new_embed = discord.Embed(
        colour=discord.Colour.dark_teal(),
        description=f':trophy: {winner} has won!',
    )
    else:
        new_embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=f"{player1} uses {move1} against {player2} for {damage1} \n {player2} uses {move2} against {player1} for {damage2}",
        )
    new_embed.add_field(name=player1,value= str(value1)+"/100")
    new_embed.insert_field_at(0,name=player2,value=str(value2)+"/100")
    return new_embed, value1, value2

class Minigame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx, *,member: discord.Member):
        await ctx.send(f'Hello {member.name} i made this changes')

    
    @commands.command()
    async def fight(self,ctx):
        author = ctx.author.display_name
        display_name = ctx.message.mentions[0].display_name
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=":boom: The battle has started!",
        )
        embed.add_field(name=author,value="100/100")
        embed.insert_field_at(0,name=display_name,value="100/100")
        value1 = 100
        value2 = 100
        message = await ctx.send(embed=embed) 
        while(value1 > 0 and value2 >0):
            new_embed, value1, value2 = editor(embed,value1,value2,author,display_name)
            await asyncio.sleep(6)
            await message.edit(embed=new_embed)
    @commands.command()
    async def who(self,ctx):
        author = ctx.author
        author_name = author.display_name
        if ctx.message.mentions:
            display_name = ctx.message.mentions[0].display_name
        await ctx.send(f"That's {display_name} and you are {author_name}")

       
    

async def setup(bot):
    await bot.add_cog(Minigame(bot))








        
'''
    @bot.command()
    async def extract(ctx):
        image = 'maps/haggle.png'
        file = discord.File(image)
        channel_id = bot.get_channel(1165731670524166184)
        message = await channel_id.send(file=file)
        image_url = message.attachments[0].url
        await ctx.send(image_url)


'''

    

 