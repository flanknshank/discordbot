import asyncio
import discord
from discord.ext import commands

class Minigame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx, *,member: discord.Member):
        await ctx.send(f'Hello {member.name} i made this changes')
async def setup(bot):
    await bot.add_cog(Minigame(bot))


'''

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
        image = 'https://cdn.discordapp.com/attachments/1162519403401859263/1165389464269496331/031.png?ex=6546ac84&is=65343784&hm=d0c851533c793e0b497d0b235c98854f7ba3f83344e7c9cc7f0707c410ca74c8&'
        embed = discord.Embed(
            colour=discord.Colour.dark_teal(),
            description=":arrow_backward: __time__ throws a spear at __aymekiwi__ for __18__ dmg! \n :arrow_forward: __aymekiwi__ wallops __time__ with a club for __20__ dmg!",
        )
        embed.add_field(name='aymekiwi',value="100/100")
        embed.insert_field_at(0,name='time',value="100/100")
        value1 = 100
        value2 = 100
        i = 2
        message2 = await ctx.send(image)
        message = await ctx.send(embed=embed) 
        while(value1 > 0 and value2 >0):
            new_embed, value1, value2 = editor(embed,value1,value2)
            await asyncio.sleep(2)
            if(i%2 == 0):
                image = 'https://cdn.discordapp.com/attachments/1162519403401859263/1165385244166336602/barnacle.png?ex=6546a896&is=65343396&hm=dbec87d6d93d5abd06f0972385a323063f2830f8c057773207fb1968401a4330&'
            else:
                image ='https://cdn.discordapp.com/attachments/1162519403401859263/1165389464269496331/031.png?ex=6546ac84&is=65343784&hm=d0c851533c793e0b497d0b235c98854f7ba3f83344e7c9cc7f0707c410ca74c8&'
            i +=1
            await message.edit(embed=new_embed)
            await message2.edit(content=image)
        

    @bot.command()
    async def extract(ctx):
        image = 'maps/haggle.png'
        file = discord.File(image)
        channel_id = bot.get_channel(1165731670524166184)
        message = await channel_id.send(file=file)
        image_url = message.attachments[0].url
        await ctx.send(image_url)


'''

    

 