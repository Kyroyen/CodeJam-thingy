import disnake
from disnake.ext import commands

from Blackhole.blackhole_functions import BlackFunction

intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    
@bot.command()
async def summary(ctx, foc:foc: str, limit: int = 100):
    messages = await ctx.channel.history(limit=limit).flatten()
    messages.reverse()
    logs = ""
    for message in messages:
        logs += f"{message.author.name} said  {message.content}."
    await ctx.send(summary(logs,foc))
