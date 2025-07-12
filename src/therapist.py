# therapist.py

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load .env file — adjust path if needed
load_dotenv()

# Create Gemini client
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"

# System prompt for the therapist bot
system_instruction = types.Part(text="""
You are a psychotherapist with a PhD in neuroscience. 
You are trained in CBT and behavioral therapy techniques. 
You help users reflect by asking thoughtful questions and being supportive.
""")

def get_response(user_input, history=[]):
    contents = history + [types.Content(role="user", parts=[types.Part(text=user_input)])]

    config = types.GenerateContentConfig(
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

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model, contents=contents, config=config
    ):
        if chunk.text:
            response_text += chunk.text or ""

    # Update history
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
    history.append(types.Content(role="model", parts=[types.Part(text=response_text)]))

    return response_text, history
