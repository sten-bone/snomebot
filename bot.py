import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from random import randint

DICE = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:']

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
    members = '\n - '.join([f'{member.name} ({member.top_role})' for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.command(name='hello', help='Responds to a message.')
@commands.has_role('admin')
async def hello(context):
    # context is a Context object
    await context.send(f"Howdy {context.message.author.mention}!")

@bot.command(name='roll', help='Roll 2d6.')
async def roll(context):
    author = context.message.author.mention
    one, two = roll_dice()
    await context.send(f"{author}\n**Result :game_die:**\n{show_die(one)} {show_die(two)}")

# roll 2d6 and return results
def roll_dice():
    return randint(1,6), randint(1, 6)

# return string representation of dice
def show_die(pips : int):
    return DICE[pips - 1]

# handle errors from on_message()
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

# handle command errors
@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.errors.CheckFailure):
        await context.send(f"Sorry {context.message.author.mention}, you do not have permission to use this command.")

bot.run(TOKEN)