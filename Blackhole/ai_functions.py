from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from typing import List

from ai21.models.chat.chat_completion_response import ChatCompletionResponse
from ai21.models.responses.summarize_response import SummarizeResponse
from dotenv import load_dotenv
import os

load_dotenv()

AI21_API_KEY = os.environ.get("AI21_API_KEY")

class A21_Functions:

    client = AI21Client(api_key=AI21_API_KEY)
    
    function_maps = {
        "simple": "base_get_format_summary",
        "key" : "key_points_extractor",
        "bullets":"bullets_points_extractor",
        "abstract":"abstract_writing_summary",
        "headline":"headline_maker",
        "swot":"swot_analyser",
        "three":"three_sentence_analyser",
        "qna":"qna_format",
        "pyramid":"inverted_pyramid_summary",
    }   
    
    initial_system_messages = [
        ChatMessage(role = "system", content="You have the spirit of a dead end job worker that is not interested in things"),
        ChatMessage(role = "system", content="You have to summarize the messages in the following format"),
    ]
    
    @classmethod
    def turn_into_message_objects(cls, message:str, role:str = "user"):
        return ChatMessage(role = role, content= message)
    
    @classmethod
    def base_get_format_summary(cls, user_messages:List[str], summarization_techique: str = "Summarize in 15 words"):
        user_message_objects = [
            cls.turn_into_message_objects(i) for i in user_messages
        ]
        
        messages = cls.initial_system_messages + \
            [cls.turn_into_message_objects(message=summarization_techique, role = "system")] + \
            user_message_objects
            
        chat_completions: ChatCompletionResponse = cls.client.chat.completions.create(
            messages=messages,
            model="jamba-instruct-preview",
        )
        
        # print( chat_completions.to_dict())
        # print(chat_completions)
        
        return chat_completions.choices[0].message.content
    
    
    @classmethod
    def key_points_extractor(cls, user_messages:List[str]):
        summarization_techique = "Identify the main ideas or key points in the message. Metion then in a list of points and explain in a highly concise manner."
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def bullets_points_extractor(cls, user_messages:List[str]):
        summarization_techique = "Identify the key points in the message. Make a list of these 2 to 4 word bullet points"
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def abstract_writing_summary(cls, user_messages:List[str]):
        summarization_techique = "Write a brief paragraph under 20 words that encapsulates the core message. Focus on the purpose, important details, and conclusion. Like abstract in a research paper"
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def headline_maker(cls, user_messages:List[str]):
        summarization_techique = "Create a headline that captures the essence of the message. Add a brief elaboration if necessary."
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def swot_analyser(cls, user_messages:List[str]):
        summarization_techique = "Do a SWOT Analysis. Identify Strengths, Weaknesses, Opportunities, and Threats. Summarize the message in terms of these four categories and mention them in individual points. Keep under 45 words"
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def three_sentence_analyser(cls, user_messages:List[str]):
        summarization_techique = "Do analysis using Three-Sentence Rule. Condense the message into three sentences: the main point, supporting details, and conclusion and mark them. This forces brevity and clarity."
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    @classmethod
    def qna_format(cls, user_messages:List[str]):
        summarization_techique = "Do analysis in a Question and Answer Format. Convert the message into a series of questions and answers under 40 words. This helps in breaking down the content into manageable parts. Just like FAQ or an interview."
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
        
    @classmethod
    def inverted_pyramid_summary(cls, user_messages:List[str]):
        summarization_techique = "Do analysis in form of an Inverted Pyramid. Make individual points. Start with the most important information and follow with less critical details and make points. Make between 2-4 points, and keep under 35 words in total. As used in journalism. For example the how news summaries or press releases are written."
        return cls.base_get_format_summary(
            user_messages=user_messages,
            summarization_techique = summarization_techique
        )
        
    

    @classmethod
    def summary(cls,text,foc):
        response: SummarizeResponse = cls.client.summarize.create(
            source_type="TEXT",
            source=text,
            focus=foc
        )
        r = response.to_json()
        i = r.find("summary")
        i += 11
        r = r[i:]
        end = r.find('"')
        r = r[:end]
        return r.replace(r'\n',"\n")
    
# intents = disnake.Intents.default()
# intents.message_content = True  # Enable access to message content

# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name} ({bot.user.id})')

# @bot.command()
# async def get_logs(ctx,foc: str, limit: int = 100):
#     """Fetches the last `limit` messages from the channel."""
#     messages = await ctx.channel.history(limit=limit).flatten()
#     messages.reverse()
#     logs = ""
#     for message in messages:
#         logs += f"{message.author.name} said  {message.content}."
#     # Split logs into chunks of 2000 characters
#     await ctx.send(summary(logs,foc))

# bot.run("APP TOKEN")

if __name__=="__main__":
    print(A21_Functions.base_get_format_summary(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.key_points_extractor(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.bullets_points_extractor(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.abstract_writing_summary(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.headline_maker(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.swot_analyser(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.three_sentence_analyser(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.qna_format(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
    print(A21_Functions.inverted_pyramid_summary(user_messages=["If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities."]))
