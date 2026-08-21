import os
from google import genai
from google.genai import types

MODEL = os.getenv("GENAI_MODEL", "gemini-2.5-flash-lite")

def generate_answer(question:str, context:str) -> str:
    if os.getenv("MOCK_LLM", "false").lower() == "true":
        return "This is a mock answer."

    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
    client = genai.Client(vertexai=True, project=project, location=location)
    system = open("prompts/system.txt", encoding='utf-8').read()
    prompt = f"{system}\n\nCONTEXT:\n{context}\n\nQUESTION:\n{question}"
    response = client.models.generate_content(
        model = MODEL,
        contents = prompt,
        config = types.GenerateContentConfig(temperature=0, max_output_tokens=350)
    )
    return response.text