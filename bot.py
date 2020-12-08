import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents)
token = "token here"

@bot.event
async def on_ready():
    print("Ready!")
    
bot.run(token)
