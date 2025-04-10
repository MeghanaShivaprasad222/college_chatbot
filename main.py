from router import route_query

print("🎓 Welcome to the College Chatbot!")
print("Ask about college info, events, or FAQs.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break
    response = route_query(user_input)
    print("Bot:", response)
