import discord
from discord.ext import commands
import pyjokes


intents = discord.Intents.default()
intents.message_content = True

token = "YOUR_TOKEN_THERE"

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event

async def on_message(ctx):
	msg = ctx.content
	if "ibragim" in msg.lower():
		joke = pyjokes.get_joke(language="en", category="all")
		await ctx.reply(joke)

bot.run(token)
