import discord
import asyncio
from discord.ext import commands #Returns a warning, not sure why - // Commands
import random
from random import randint
 #For use in dice rolling
import sys #Safety feature for shutting down the bot, so I've read
bot = commands.Bot(command_prefix='^')
"""
Trying to follow good practice
with Bot command calls. Simply using:
'!', '?', '.', etc., is problematic.
https://github.com/meew0/discord-bot-best-practices
"""
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
    results=[]
    for role in range(1):
        x=random.randint(1,die)
        results.append(x)
        embedVar=discord.Embed(title = "You rolled a D" + str(die), description = "And you got " + str(results) +"!")
        embedVar.color=discord.Color.dark_gold()
    await ctx.send(embed=embedVar)
    ##} Allows the user to roll a single die // ^d 100 - returns value // ^d 20 - returns value // so on.
    """
    An issue I have with most of these commands is that anytime
    I call some time of int or value immediately after the "command" caller
    itself, a space char is *absolutely* required. I can't find a
    way around it. Makes the command "^d 20", rather than "^d20"
    I feel the latter is more user friendly, but I don't know how
    to work it in.
    """
    ##===End-Dice-Commands==##
@bot.event
async def on_ready():
    activity=discord.Game("Rolling for Innitiative!")
    await bot.change_presence(status=discord.Game.idle, activity=activity)
###]-^Last I checked this doesn't work
### But hell, figured i'd leave it in case 
### it comes in handy
## -----------------------------------------
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

#@bot.command() # allows users to test the response of the bot from Discord
#async def test(ctx):
#    await ctx.send('Ready to roll!'.format(ctx.author))
#
@bot.command() # shuts down the bot
async def stop(ctx):
    await ctx.send(("Logging out. See you next session!").format(ctx.author))
    sys.exit()

bot.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.tp2tlQU4e8GdwvCGYtmHM1Xaalw')