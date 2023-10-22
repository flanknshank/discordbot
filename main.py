import settings
import discord
import simplecommands
import timeZone
from cogs.minigame import Minigame
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        await bot.load_extension("cogs.minigame")
    
    @bot.command()
    async def reload(ctx):
        await bot.unload_extension("cogs.minigame")
        await bot.load_extension("cogs.minigame")
        await ctx.send("File has been reloaded")
        
    simplecommands.setup(bot)
    timeZone.setup(bot)
    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()