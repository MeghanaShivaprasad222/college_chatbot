from intent_router import classify_intent
from agents.prompts import info_prompt, event_prompt, faq_prompt
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

def route_query(user_query: str) -> str:
    intent = classify_intent(user_query)
    
    if intent == "info":
        chain = LLMChain(llm=llm, prompt=info_prompt)
    elif intent == "event":
        chain = LLMChain(llm=llm, prompt=event_prompt)
    elif intent == "faq":
        chain = LLMChain(llm=llm, prompt=faq_prompt)
    else:
        return "Sorry, I didn't understand your request."

    return chain.run(question=user_query)

def route_query(user_input):
    # logic using LangGraph or LangChain
    return "This is a dummy response"  # Replace with real logic
