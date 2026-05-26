import discord
from discord.ext import commands

# Carica le variabili d'ambiente dal file .env
import os
from dotenv import load_dotenv

load_dotenv()

# creare i permessi per il nostro bot
intents = discord.Intents.default()
intents.message_content = True

# Creiamo il bot
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Il bot{bot.user} e' online")


@bot.command()
async def lista_comandi(ctx):
    lista_comandi = {
        "consigli_ricerca_materiali": "Questo comando permette di ricevere consigli sui materiali",
        "consigli_costruzione": "Questo comando permette di ricevere consigli sulla costruzione",
    }
    messaggio = "Ecco la lista dei comandi disponibili:\n"
    for comando, descrizione in lista_comandi.items():
        messaggio += f"{comando}: {descrizione}\n"
    await ctx.send(messaggio)


@bot.command()
async def consigli_ricerca_materiali(ctx):
    lista_consigli = [
        "Esplora le caverne per trovare minerali preziosi come diamanti e oro.",
        "Cerca nelle foreste per raccogliere legno e risorse naturali.",
        "Esplora i villaggi per trovare risorse e scambiare con i mercanti."
    ]
    await ctx.send("Consigli per la ricerca di materiali:\n" + "\n".join(lista_consigli))


@bot.command()
async def consigli_costruzione(ctx):
    lista_consigli = [
        "Pianifica la tua costruzione prima di iniziare.",
        "Utilizza materiali resistenti per creare strutture durature.",
        "Assicurati di avere uno stock sufficiente di risorse."
    ]
    await ctx.send("Consigli per la costruzione:\n" + "\n".join(lista_consigli))

# comando per.....





# Legge il token da una variabile d'ambiente
token = os.getenv('DISCORD_TOKEN')


bot.run(token)

