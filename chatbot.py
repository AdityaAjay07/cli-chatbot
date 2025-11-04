from openai import OpenAI

# Initialize the OpenAI client (make sure your API key is set as an environment variable)
client = OpenAI()

print("💬 Vibe Code: CLI Chat Program")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly AI assistant for a CLI chatbot project."},
            {"role": "user", "content": user_input},
        ]
    )

    print("Bot:", response.choices[0].message.content)
