import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# allows bot to access members
botIntents = discord.Intents.default()
botIntents.members = True

# client = discord.Client(intents=botIntents)
bot = commands.Bot(command_prefix="sb ", intents=botIntents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    
    print(f'{bot.user} has connected to Guild: {guild.name}!')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    print(message)
    await message.channel.send("Thanks for the message!")

# handle errors from on_message()
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.run(TOKEN)