from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4-mini")

result = llm.invoke("What is the current time in India?")

print(result)

