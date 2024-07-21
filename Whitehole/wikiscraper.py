import disnake
from disnake.ext import commands
import requests
from bs4 import BeautifulSoup


# Bot setup
intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)

def scrape_wiki_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the title of the page
    title = soup.find(id="firstHeading").text

    # Get the first 10 lines of the content
    content_paragraphs = soup.find(id="bodyContent").find_all("p")
    content = "\n".join([p.text for p in content_paragraphs[:3]])  # Adjust the number of paragraphs as needed
    lines = [line for line in content.split("\n") if line.strip() != '']  # Filter out empty lines
    first_600_chars = (''.join(lines))[:600] + "..."  # Get the first 600 characters and append "..."

    # Find the first link to another wiki article
    all_links = soup.find(id="bodyContent").find_all("a", href=True)
    next_link = None
    for link in all_links:
        href = link['href']
        if href.startswith("/wiki/") and not href.startswith(("/wiki/Special:", "/wiki/Help:", "/wiki/Wikipedia","/wiki/File","/wiki/Category","/wiki/Template")) and title.upper() not in href.upper():
            #print(href) for debugging
            next_link = "https://en.wikipedia.org" + href
            break

    return title, first_600_chars, next_link

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.slash_command(description="Ask the bot for a Wikipedia summary")
async def ask(inter, noun: str):
    await inter.response.defer()  # Defer the response to give more time for processing
    url = f"https://en.wikipedia.org/wiki/{noun}"
    iterations = 3

    response_content = []

    for i in range(iterations):
        title, content, next_link = scrape_wiki_article(url)
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





token = open("authtk.txt",'r').read()
bot.run(token)

