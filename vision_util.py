import base64
from openai import OpenAI
from config import OPENAI_API_KEY, VISION_MODEL

openai_client = OpenAI(api_key="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")
##  Temp going to just use the api key instead of putting it in config##

def encode_image_to_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def analyze_two_images(baseline_path: str, new_path: str) -> str:
    b64a = encode_image_to_b64(baseline_path)
    b64b = encode_image_to_b64(new_path)
    messages = [
        {
            "role": "system",
            "content": "You are an assistant that compares two shelf images. Determine what items are currently on the shelf, and what changed (added, removed, count changes). Respond in Markdown."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Compare these two shelf images and describe what changed and what is currently on the shelf:"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{b64a}"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{b64b}"}
            ],
        }
    ]
    resp = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500
    )
    output = resp.choices[0].message["content"]
    print("GPT Response:", output)  # For debugging
    return output


    
