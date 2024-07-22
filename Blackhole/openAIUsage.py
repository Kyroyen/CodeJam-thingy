from openai import OpenAI
from dotenv import load_dotenv
import os

API_KEY = os.environ.get("OPENAI_API_KEY")
# print("API_KEY",API_KEY)
client = OpenAI()


class WhiteHole:

    @classmethod
    def white_hole_basic(cls, user_message: str):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a rude bot, with attitude of a deadend job worker."},
                {"role": "system", "content": "Your job is to summarize the message given by the user in a highly oversimplified and consice manner"},
                {"role": "user", "content": user_message}
            ]
        )

if __name__=="__main__":
    print(WhiteHole.white_hole_basic('''i\'ll drop it into brainstorm?. i was thinking maybe we can create seperate discussions for these two the two categories: info spam and non info spam. for now, i'll dump it into brainstorm since i don't have perms'''))
