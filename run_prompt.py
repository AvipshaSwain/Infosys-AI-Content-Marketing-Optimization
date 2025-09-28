import base64
from google import genai
from google.genai import types



GEMINI_API_KEY = "AIzaSyDFx778OgexyAj8ekqRy6OQSVOw1B2YeX8"
# Function for tweet creation
def execute_gemini_for_tweet_creation(prompt, model, thinking_budget=0):
    client = genai.Client(api_key=GEMINI_API_KEY)

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["tweet"],
            properties={
                "tweet": genai.types.Schema(type=genai.types.Type.STRING),
            },
        ),
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text  # JSON string


# Function for tweet prediction (comparison)
def execute_gemini_for_tweet_prediction(prompt, model, thinking_budget=0):
    client = genai.Client(api_key=GEMINI_API_KEY)

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=thinking_budget,
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["tweet_a_vs_tweet_b", "prediction", "explanation"],
            properties={
                "tweet_a_vs_tweet_b": genai.types.Schema(type=genai.types.Type.STRING),
                "prediction": genai.types.Schema(type=genai.types.Type.STRING),
                "explanation": genai.types.Schema(type=genai.types.Type.STRING),
            },
        ),
    )
    

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text  # JSON string
