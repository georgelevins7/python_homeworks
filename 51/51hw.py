from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

chat_history = []

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
user_input = ""
while True:
    user_input = input("Enter your question: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    if user_input.lower() == "history":
        for message in chat_history:
            role = message["role"]
            text = message["parts"][0]["text"]
            print(f"{role.upper()}: ")
            print(text)
        continue
    chat = client.chats.create(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=
            "You are an experienced senior software engineer and programming mentor. " \
            "Explain technical concepts clearly, adapt your explanations to the user's level." \
            "Use practical examples when appropriate." \
            "Maximum 3 short sentences."
            "Context: Clear explaining for future developers in a concise and understandable manner." \
            "Use code examples when appropriate.",
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
            max_output_tokens=1000,
            temperature=0.2,
        ),
        history=chat_history
    )

    response = chat.send_message(user_input)
    print(response.text)
    chat_history.append({
        "role": "user",
        "parts": [{
            "text": user_input
        }]
    })
    chat_history.append({
        "role": "model",
        "parts": [{
            "text": response.text
        }]
    })