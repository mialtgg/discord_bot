import discord
from discord.ext import commands
import json

#  config.json dosyası
{
  "token": "token"
}


# config dosyasını oku
with open('config.json') as config_file:
    config_data = json.load(config_file)

# token'ı al
token = config_data["token"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yaptık: {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Merhaba {ctx.author.name}!')

# Botu çalıştırın
bot.run(token)

