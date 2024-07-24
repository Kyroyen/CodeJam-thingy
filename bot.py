import disnake
from disnake.ext import commands

from Blackhole.blackhole_functions import BlackFunction

intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    
@bot.command()
async def summary(ctx, arg):
    
    await ctx.send(arg)