import asyncio
import discord

def editor(new_embed, value1,value2):
    value1 = value1 -20
    value2 = value2 - 5
    if value1 <= 0 or value2 <= 0:
        new_embed = discord.Embed(
        colour=discord.Colour.dark_teal(),
        description=":arrow_backward: __time__ throws a spear at __aymekiwi__ for __18__ dmg! \n :arrow_forward: __aymekiwi__ wallops __time__ with a club for __20__ dmg! \n :trophy: time has won!",
    )
    else:
        new_embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=":arrow_backward: __time__ throws a spear at __aymekiwi__ for __18__ dmg! \n :arrow_forward: __aymekiwi__ wallops __time__ with a club for __20__ dmg!",
        )
    new_embed.add_field(name='aymekiwi',value= str(value1)+"/100")
    new_embed.insert_field_at(0,name='time',value=str(value2)+"/100")
    return new_embed, value1, value2


def setup(bot):  
    @bot.command()
    async def edit(ctx):
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=":arrow_backward: __time__ throws a spear at __aymekiwi__ for __18__ dmg! \n :arrow_forward: __aymekiwi__ wallops __time__ with a club for __20__ dmg!",
        )
        embed.add_field(name='aymekiwi',value="100/100")
        embed.insert_field_at(0,name='time',value="100/100")
        value1 = 100
        value2 = 100
        message = await ctx.send(embed=embed)
        while(value1 > 0 and value2 >0):
            new_embed, value1, value2 = editor(embed,value1,value2)
            await asyncio.sleep(2)
            await message.edit(embed=new_embed)
        






    

 