# Shelf Vision Discord Bot

This is a starter template for a Discord bot that compares two shelf images (baseline + current), uses a vision + language model to detect what’s on the shelf and what changed, then posts a Markdown report into Discord.

## Features

- Accepts two images, sends them to a vision-enabled LLM, and asks it to compute changes + current inventory  
- Posts results into Discord (via a bot command) in Markdown  
- Has utility modules for diffing and formatting  

## Requirements

- Python 3.10+  
- OpenAI API access to a vision-capable model  
- A Discord bot token (with message send / read permissions)  
- (Optional) Webhook support  

## Setup

1. Clone this repo  
2. Create a `.env` or set environment variables for:
   - `OPENAI_API_KEY`
   - `DISCORD_BOT_TOKEN`
   - `VISION_MODEL` (e.g. `gpt-4-vision-preview` or whatever model you have)  
   - `DISCORD_WEBHOOK_URL` (if using webhook instead of bot)  

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
