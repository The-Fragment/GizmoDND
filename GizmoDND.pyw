import discord
import asyncio
from discord.ext import commands #Returns a warning, not sure why - // Commands
from discord.ext.commands import bot
import traceback
import time
import random
from random import randint#For use in dice rolling
import sys #Safety feature for shutting down the bot, so I've read
from discord.utils import get
import urllib.parse, urllib.request, re
import time
import re
#/////////// Start Up, "Front End" /////////////
bot = discord.Client()
bot = commands.Bot(command_prefix='^')
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
async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('Depression in VR'))
        await asyncio.sleep(30)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with Jays mom'))
        await asyncio.sleep(30)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('Cat Simulator 2'))
        await asyncio.sleep(30)
        #await bot.change_presence(status=discord.Status.online, activity=discord.ActivityType.watching('for ^help'))
        #await asyncio.sleep(10)
       # await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity('rolling a ^d 20'))
        #await asyncio.sleep(10)
        #await bot.change_presence(status=discord.Status.dnd, activity=discord.ActivityType.watching('for sus members...'))
       # await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Playing Genshin Impact'))
        await asyncio.sleep(30)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('osu!'))
        await asyncio.sleep(30)
        #commented out code that doesn't seem to work. Docs said it should, but I dunno.
        #leaving it in there just in case, because we may need it later
    
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print("Ready to roll!")
    print("--------------")
    print (time.strftime("Time at start:\n"+"%H:%M:%S"))

    #await client.change_presence(status=discord.Status.dnd, activity=discord.ActivityType.watching('Star Wars')) -- Alternatives,
    # You've gotta lot of options with these

#///////////////// End "Front End" ///////////////////////

@bot.command()
async def dev(ctx):

     devEmbed = discord.Embed(title="Developers:", description= "**These peeps worked to bring me to me to what I am today:**\n" 
                                 +"\nflop#2371\nSeltzer#0006\nklb#5169\n\n"
                                 +"**Version:**\t 0.0.0\n"
                                 +"**Date Released:** \t N/A",color=discord.Color.purple())
       
     await ctx.send(embed=devEmbed)                                            
    #playing with embeds
#////// Who's who: ///////
async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await ctx.send(to_send)
    
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please use proper formatting. Use ^help for more info.')


##[Start-Dice-Functions]##
@bot.command(pass_context=True)
async def r(ctx, roll:str):
     results = 0
     resultString=''
     try:
         try:
             numDice=roll.split('d')[0]
             diceVal=roll.split('d')[1]
         except Exception as e:
             print (e)
             await ctx.send("Use proper format! #d# %s." % (ctx.author.mention))
             return
         if int(numDice)>500:
             await ctx.send("Woah! too much!" % (ctx.author.mention))
             return
            
         await ctx.send("Rolling %s d%s for %s" %(numDice, diceVal, ctx.message.author.name))
         rolls, limit = map(int,roll.split('d'))
         for r in range(rolls):
             number = random.randint(1, limit)
             results = results + number
             if resultString == '':
                 resultString += str(number)
             else:
                resultString +=', '+ str(number)

         if resultString == '20':
             await ctx.send((ctx.author.mention)+ "  :game_die:\n**Critical Success!** " + resultString)
         else:
             if resultString == '1':
                 await ctx.send((ctx.author.mention)+ "  :game_die:\n**Critical Failure!** " + resultString)
             else:


                 if numDice =='1':
                     await ctx.send((ctx.author.mention)+ "  :game_die:\n**Result:** " + resultString)
                 else:
                     await ctx.send((ctx.author.mention)+"  :game_die:\n**Result:** " + resultString + "\n**Total:** " + str(results))

     except Exception as e:
         print (e)
         return

    # for role in range(amount):
   #   x = random.randint(1, dice_type)
   #   results.append(x)
   #   embedVar=discord.Embed(title="You rolled " +str(amount)+" D"+str(dice_type)+ "'s",description   = "\n***And here is your results....***\n\n\n"+str(results))
   #   embedVar.color=discord.Color.purple()
     
    ##}} Allows the users to call a command as such: ^roll 2 20 // will Return value of 2 D20 die {{##
@bot.command(pass_context=True, description= 'Roll a single Die: (Prefix)d (Die) // !d 20, returns a d20 roll')
async def d(ctx, die:int):
         results=[]
         for role in range(1):
            x=random.randint(1,die)
            results.append(x)
            embedVar=discord.Embed(title = "You rolled a D" + str(die), description = "And you got " + str(results) +"!")
            embedVar.color=discord.Color.dark_gold()
            await ctx.send(embed=embedVar)
  
   ##Allows the user to roll a single die // ^d 100 - returns value // ^d 20 - returns value // so on.
   ##Would like some kinda error handle^
   ##############################################################################
   # An issue I have with most of these commands is that anytime                #
   # I call some time of int or value immediately after the "command" caller    #
   # itself, a space char is *absolutely* required. I can't find a              #
   # way around it. Makes the command "^d 20", rather than "^d20"               #
   # I feel the latter is more user friendly, but I don't know how              #
   # to work it in.                                                             #
   ##############################################################################
    ##===End-Dice-Commands==##

############## Purge #######################
@bot.command(pass_context=True, description='Purge the messages of a channel / Admin Perms.')
@commands.bot_has_permissions(administrator=True)
async def purge(ctx,limit:int):
    await ctx.channel.purge(limit=limit+1)
    await asyncio.sleep(2)
    await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention)) 
##^Just purges stuff pretty much
@purge.error ##Simple error checking
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ha! You're not worthy!")
###------Gonna worry about this one later lol----------------------------------------

@bot.command() # allows users to test the response of the bot from Discord
async def test(ctx):
    await ctx.send('Ready to roll!'.format(ctx.author))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

#///////////Test/////////////////////
#////////////////////////////////////
@bot.command() # shuts down the bot
async def stop(ctx):
    await ctx.send(("Logging out. See you next session!").format(ctx.author))
    sys.exit()

bot.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.tp2tlQU4e8GdwvCGYtmHM1Xaalw')