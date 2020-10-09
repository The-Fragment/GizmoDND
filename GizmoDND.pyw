import discord
from .enums import ActivityType, try_enum
import asyncio
from discord.ext import commands #Returns a warning, not sure why - // Commands
from discord.ext.commands import bot
import traceback
import time
import random
from random import randint#For use in dice rolling
import sys #Safety feature for shutting down the bot, so I've read
#///////////

client = discord.Client()
bot = commands.Bot(command_prefix='^')
#messages = joined = 0 // for stats

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


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
#### Not working presently, will leave in case it becomes useful(other funcs removed):
#@client.event #also for stats, but does things i think. Needs testing
#async def on_member_join(member): 
#    global joined
#    joined += 1
#    for channel in member.server.channels:
#        if str(channel)=="general":
#            await client.send_message(f"""Welcome {member.mention}!""")
#
#-------->

##[Start-Dice-Functions]##
@bot.command(pass_context=True, description='Roll multiple Dice: (Prefix)roll (Ammount) (Die) // !roll 3 20, returns three D20 rolls')
async def roll(ctx,amount:int,dice_type:int):
     results = []
     for role in range(amount):
        x = random.randint(1, dice_type)
        results.append(x)
        embedVar=discord.Embed(title="You rolled " +str(amount)+" D"+str(dice_type)+ "'s",description   = "\n***And here is your results....***\n\n\n"+str(results))
        embedVar.color=discord.Color.purple()
        
     await ctx.send(embed=embedVar)
    ##}} Allows the users to call a command as such: ^roll 2 20 // will Return value of 2 D20 die {{##
@bot.command(pass_context=True, description= 'Roll a single Die: (Prefix)d (Die) // !d 20, returns a d20 roll')
async def d(ctx, die:int):
    try:
         results=[]
         for role in range(1):
            x=random.randint(1,die)
            results.append(x)
            embedVar=discord.Embed(title = "You rolled a D" + str(die), description = "And you got " + str(results) +"!")
            embedVar.color=discord.Color.dark_gold()
            await ctx.send(embed=embedVar)
    except:
        ctx.send('Something must have gone wrong! Make sure to use proper format, use the help command if you need to check for valid syntax {} '.format(ctx.author.mention))
   ##Allows the user to roll a single die // ^d 100 - returns value // ^d 20 - returns value // so on.
   ##Try / Catch isn't working
   ##Would like some kinda error handle
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
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention)) 
##^Just purges stuff pretty much
@purge.error ##Simple error checking
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ha! You're not worthy!")
##----------------------------------------------
@bot.event # says when the bot should be ready as a message in VS's CL
async def on_ready():
    print("Ready to roll!")
    print("--------------")
    print (time.strftime("Time at start:\n"+"%H:%M:%S"))

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



#-------------------------------------------------------
#Stat Blocks::::::::::::::::: Not Working in the Slightest, from my testing -- Will leave in case it's useful
#async def update_stats():
#    await client.wait_until_ready()
#    global messages, joined
#
#    while not client.is_closed():
#        try:
#            with open("stats.txt", "a") as f:
#                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
#            messages = 0
#            joined = 0
#            await asyncio.sleep(5)
#        except Exception as e:
#            print(e)
#            await asyncio.sleep(5)
#End Stat blocks
###----------------







@bot.command() # shuts down the bot
async def stop(ctx):
    await ctx.send(("Logging out. See you next session!").format(ctx.author))
    sys.exit()
bot.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.tp2tlQU4e8GdwvCGYtmHM1Xaalw')