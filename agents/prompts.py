from langchain.prompts import PromptTemplate

info_prompt = PromptTemplate.from_template(
    "You are a college info assistant. Answer clearly and helpfully.\n\nQuestion: {question}\nAnswer:"
)

event_prompt = PromptTemplate.from_template(
    "You are an event assistant. Fetch and summarize today's events from the event database.\n\nUser: {question}\nAnswer:"
)

faq_prompt = PromptTemplate.from_template(
    "You are a helpful FAQ bot. Answer the student's common queries as accurately as possible.\n\nQuery: {question}\nAnswer:"
)

