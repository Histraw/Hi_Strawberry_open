import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event 
async def on_ready():
    print(">> 機器人已就緒 <<")

bot.run('ODI3NDA4MTA5OTY1NjcyNDQ4.YGal2Q.XvGobd_yo309XzzygYtGnP21QJQ')