from langchain.chat_models import ChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

intent_prompt = PromptTemplate.from_template(
    """Classify the intent of the user query into one of the following categories: info, event, faq.

Query: "{query}"
Intent:"""
)

intent_chain = LLMChain(llm=llm, prompt=intent_prompt)

def classify_intent(query: str) -> str:
    result = intent_chain.run(query=query).strip().lower()
    return result
