import discord
import os
import asyncio
from discord.ext import commands  # Returns a warning, not sure why - // Commands
from discord.ext.commands import bot
import sys  # Safety feature for shutting down the bot, so I've read
import time
from GizmoCommands import *
import requests
from bs4 import BeautifulSoup
from cogs import *


def get_prefix(bot, message):
    """should be a callable prefix, allow perserver"""
    prefixes = ['^','jizz','>>']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)
"""Only allow ? in DM, If we're in a guild allows for Bot mention or Prefix in List"""
inital_extensions = ['cogs.dnd',
                     'cogs.admin',
                     'cogs.utility',
                     'cogs.fun']
bot = commands.Bot(command_prefix=get_prefix, description='Testing this function')
if __name__=='GizmoDND':
    for extension in inital_extensions:
        bot.load_extension(extension)
#bot = commands.Bot(command_prefix='^')
bot.remove_command('help')
intents = discord.Intents.default()
intents.members = True
"""
Trying to follow good practice
with Bot command calls. Simply using:
'!', '?', '.', etc., is problematic.
https://github.com/meew0/discord-bot-best-practices
---
Helpful:
https://github.com/Rapptz/discord.py
"""

@bot.event
async def on_ready():
    print("Ready to roll!")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S\n"+
                        "%m/%d/%Y\n"
                        + "--------------"))
    while True:
           await bot.change_presence(status=discord.Status.online, activity=discord.Game('Depression in VR'))
           await asyncio.sleep(45)
           await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with Jays mom'))
           await asyncio.sleep(45)
           await bot.change_presence(status=discord.Status.online, activity=discord.Game('Cat Simulator 2'))
           await asyncio.sleep(45)
           await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Playing Genshin Impact'))
           await asyncio.sleep(45)
           await bot.change_presence(status=discord.Status.idle, activity=discord.Game('osu!'))
           await asyncio.sleep(45)
           await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="MEGALOVANIA"))
           await asyncio.sleep(45)
           await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Emperor's New Groove"))
           await asyncio.sleep(45)
           await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Among Us"))
           await asyncio.sleep(45)
           await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Beat Saber"))
           await asyncio.sleep(45)
           await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "For ^ || ^help"))
           await asyncio.sleep(45)


###------Gonna worry about this one later lol----------------------------------------
"""
Pretty much this function just returns a random image of a cat
Its web scraping but like its kinda lame but hey cool cats!
"""
bot.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.e0siqGflMa3jvtcfVcOYD2km4AE', bot=True, reconnect=True)
