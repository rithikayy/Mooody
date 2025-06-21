import os
from google import genai
from google.genai import types

##genai.configure(api_key="AIzaSyDBvKGqM5iQqDIVcsQElbj-vpMtKlVArP4")

def run_chatbot():
    client = genai.Client(api_key="AIzaSyDBvKGqM5iQqDIVcsQElbj-vpMtKlVArP4")
    model = "gemini-2.5-flash"

    system_instruction = types.Part(text=
        "You are a psychotherapist with a PhD in neuroscience. You have knowledge about CBT and other behavioural therapy techniques. You are patient with your clients, asking them questions to allow them to answer their own problems."
    )

    history = []

    print("🧠 Mental Health Chatbot\nType 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Build conversation context
        contents = history + [
            types.Content(role="user", parts=[types.Part(text=user_input)])
        ]

        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=-1),
            safety_settings=[
                types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
                types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
                types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
                types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
            ],
            response_mime_type="text/plain",
            system_instruction=[system_instruction],
        )

        # Stream model response
        print("Bot: ", end="", flush=True)
        response_text = ""
        for chunk in client.models.generate_content_stream(
            model=model, contents=contents, config=generate_content_config
        ):
            print(chunk.text, end="", flush=True)

            if chunk.text:
                response_text += chunk.text or ""

        print("\n")

        # Save history
        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
        history.append(types.Content(role="model", parts=[types.Part(text=response_text)]))

if __name__ == "__main__":
    run_chatbot()