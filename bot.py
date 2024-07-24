import disnake
from disnake.ext import commands
from Whitehole.whitehole_functions import WhiteFunction
from Blackhole.blackhole_functions import BlackFunction

intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    
@bot.command()
async def summary(ctx, arg):
    
    await ctx.send(arg)

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





token = open("Whitehole/authtk.txt",'r').read()
bot.run(token)

