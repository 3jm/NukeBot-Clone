import logging as log
import nextcord, os, sys
from nextcord.ext import commands
from nextcord import Interaction


# Logging config
log.basicConfig(filename='bot.log', level=log.INFO, format='[%(asctime)s] [%(msecs)dms] [%(levelname)s] : %(message)s')

# Discord Bot Token
token = ""

# Discord Bot Intents
intents = nextcord.Intents.all()

# Discord Bot Initilization
bot = commands.Bot(intents=intents)

# Discord Bot Local slash command registration
testing_guild_id = 1017999660603944960

def preRunCheck():
    log.info('===================')
    log.info('Made by Blind#6637')
    if token == "" or None:
        log.critical('No token was passed! Exiting.')
        sys.exit()
    else:
        preload_cogs()

def preload_cogs():
    log.info("Pre loading cogs...")
    initial_extensions = []
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                print('loaded ' + filename)
                initial_extensions.append("cogs." + filename[:-3])
            except Exception as e:
                print(e)

    log.info("All cogs pre loaded.")

    if __name__ == "__main__":
        for extension in initial_extensions:
            bot.load_extension(extension)
    
    Bot()

def Bot():
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f"Made by Blind#6637 | NukeBot Clone"))
        log.info('Bot is ready.')
        print("ready") 

    @bot.event
    async def on_command_error(interaction: Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            em = nextcord.Embed(
                description="you are missing required permissions to run this command."
            )
            await interaction.response.send_message(embed = em)

    try:
        log.info('Logging into bot...')
        bot.run(token)
    except Exception as e:
        log.CRITICAL('An error occured - {}'.format(e))

if __name__ == '__main__':
    preRunCheck()