import settings
import discord
import simplecommands
from discord.ext import commands


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
    simplecommands.setup(bot)


    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()