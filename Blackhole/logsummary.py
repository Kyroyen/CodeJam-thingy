from ai21 import AI21Client
from ai21.models.chat import ChatMessage
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
