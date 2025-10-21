import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("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")
VISION_MODEL = os.getenv("gpt-4-vision-preview", "gpt-4-vision-preview")

DISCORD_BOT_TOKEN = os.getenv("MTQyMDE0NDE0ODQwNDYzMzYwMA.GFfIde.vsw8JTLXzBBWhRAAm1MKCyeLciAZQIJWR-uMnM")
DISCORD_WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1429879281592303737/7QlxkVka121W2jtFKrLs1TG9QBAGySLde0AKFVNEUhKmOWwuv7zoi9YZ_Y0j7Koo7yNW", None)
