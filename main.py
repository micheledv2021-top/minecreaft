import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# creare i permessi per il nostro bot
intents = discord.Intents.default()
intents.message_content = True

# Creiamo il bot
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Il bot{bot.user} e' online")

# Legge il token da una variabile d'ambiente
token = os.getenv("DISCORD_TOKEN")
bot.run(token)

