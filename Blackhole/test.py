import disnake
from disnake.ext import commands
import logsummary
intents = disnake.Intents.default()
intents.message_content = True  # Enable access to message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def get_logs(ctx,foc: str, limit: int = 100):
    """Fetches the last `limit` messages from the channel."""
    messages = await ctx.channel.history(limit=limit).flatten()
    messages.reverse()
    logs = ""
    for message in messages:
        logs += f"{message.author.name} said  {message.content}."
    await ctx.send(summary(logs,foc))

bot.run("APP TOKEN")
