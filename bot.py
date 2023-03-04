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
	if "придумай шутку" in msg.lower():
		joke = pyjokes.get_joke(language="en", category="all")
		from deep_translator import GoogleTranslator
		translated = GoogleTranslator(source='english', target='russian').translate(joke)
		await ctx.reply(translated)
		await ctx.reply("-----------------------------------------------------")
		await ctx.reply(joke)

bot.run(token)