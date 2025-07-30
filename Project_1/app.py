import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage



try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI()
# llm.invoke("Hello, world!")


model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("Translate the following from English into Spanish:"),
    HumanMessage("Good morning, have a nice day!"),
]

print(model.invoke(messages))

