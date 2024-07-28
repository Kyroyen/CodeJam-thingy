import disnake
from disnake.ext import commands
from Whitehole.whitehole_functions import WhiteFunction 
from Blackhole.blackhole_functions import BlackFunction

from dotenv import load_dotenv
import os

load_dotenv()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='.',intents=intents)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.command()
async def summary(ctx, type: str, limit: int = 15):
    messages = await ctx.channel.history(limit=limit).flatten()
    messages.reverse()
    logs = []
    for message in messages:
        if message.author.name != bot.user:
            logs.append(f"{message.author.name} said  {message.content}.")
    
    # print(logs)
    
    black_obj = BlackFunction(
        logs
    )
    
    
    if type=="random":
        result = black_obj.get_random_summary()
    else:
        result = black_obj.get_summary(type)
    
    await ctx.send(result)

@bot.slash_command(description="Ask the bot for a Wikipedia summary")
async def ask(inter, noun: str):
    await inter.response.defer()  # Defer the response to give more time for processing
    url = f"https://en.wikipedia.org/wiki/{noun}"
    iterations = 3

    response_content = []

    for i in range(iterations):
        title, content, next_link = WhiteFunction.scrape_wiki_article(url)
        response_content.append(f"**{title}**\n{content}")

        if next_link and not i==iterations-1:#so there is not repeat of 
            response_content.append(f"And to explain {next_link.split('/wiki/')[-1].replace('_', ' ')}:")
            url = next_link
        else:
            break
    #print("\n\n".join(response_content)) for debugging
    # Send all the collected content as a single message
    await inter.followup.send("\n\n".join(response_content))

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
@bot.slash_command(description="Travel planner between two cities")
async def travel(inter,cityone,citytwo):
    citytwo=citytwo.strip()
    cityone=cityone.strip()
    await inter.response.defer()
    try:
        travel_times=WhiteFunction.findT(cityone,citytwo)
        formatted_output = '\n'.join([f'- {vehicle}: *{time}*' for vehicle, time in travel_times.items()])
        await inter.followup.send(f"**Time it will take to travel from {cityone} to {citytwo}:**\n{formatted_output}")

    except ValueError as a:
        await inter.followup.send(a)
    
    
# token = open("Whitehole/authtk.txt",'r').read()
token = os.environ.get("DISCORD_KEY")
bot.run(token)
