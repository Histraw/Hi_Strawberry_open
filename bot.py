import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event 
async def on_ready():
    print(">> 機器人已就緒 <<")

bot.run('')