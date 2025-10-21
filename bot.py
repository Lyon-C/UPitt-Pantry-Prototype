import discord
from discord.ext import commands
from vision_util import analyze_two_images
from diff_util import parse_model_markdown, diff_counts, format_diff_md
from config import DISCORD_BOT_TOKEN, DISCORD_WEBHOOK_URL

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="shelf")
async def shelf_report(ctx, baseline: str, current: str):
    """
    Usage: !shelf baseline.jpg current.jpg
    """
    try:
        md = analyze_two_images(baseline, current)
    except Exception as e:
        await ctx.send(f"Error calling vision API: {e}")
        return

    await ctx.send(md)

if True:
    @bot.command(name="shelf_webhook")
    async def shelf_via_webhook(ctx, baseline: str, current: str):
        md = analyze_two_images(baseline, current)
        import requests
        payload = {"content": md}
        try:
            resp = requests.post("https://discord.com/api/webhooks/1429879281592303737/7QlxkVka121W2jtFKrLs1TG9QBAGySLde0AKFVNEUhKmOWwuv7zoi9YZ_Y0j7Koo7yNW", json=payload)
            if resp.status_code != 204 and resp.status_code != 200:
                await ctx.send(f"Webhook error: {resp.status_code} {resp.text}")
            else:
                await ctx.send("Posted via webhook.")
        except Exception as e:
            await ctx.send(f"Error posting webhook: {e}")

if __name__ == "__main__":
    bot.run("MTQyMDE0NDE0ODQwNDYzMzYwMA.GFfIde.vsw8JTLXzBBWhRAAm1MKCyeLciAZQIJWR-uMnM")
