import disnake
from disnake.ext import commands

from Blackhole.blackhole_functions import BlackFunction

intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command()
async def summary(ctx, type: str, limit: int = 5):
    messages = await ctx.channel.history(limit=limit).flatten()
    # messages.reverse()
    logs = [f"{message.author.name} said  {message.content}." for message in messages]
    
    black_obj = BlackFunction(
        logs
    )
    
    if type=="random":
        result = black_obj.get_random_summary()
    else:
        result = black_obj.get_summary(type)
    
    await ctx.send(result)
