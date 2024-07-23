from ai21 import AI21Client
from ai21.models.chat import ChatMessage
import disnake
from disnake.ext import commands
client = AI21Client(api_key="Insert API KEY")
def summary(text,foc):
    response = client.summarize.create(
        source_type="TEXT",
        source=text,
        focus=foc
    )
    r=response.to_json()
    i=r.find("summary")
    i+=11
    r=r[i:]
    end=r.find('"')
    r=r[:end]
    return r.replace(r'\n',"\n")
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
    # Split logs into chunks of 2000 characters
    await ctx.send(summary(logs,foc))

bot.run("APP TOKEN")
