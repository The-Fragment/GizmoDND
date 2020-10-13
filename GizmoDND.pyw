import discord
import asyncio
from discord.ext import commands  # Returns a warning, not sure why - // Commands
from discord.ext.commands import bot
import random
from random import randint  # For use in dice rolling
import sys  # Safety feature for shutting down the bot, so I've read
from discord.utils import get
import time
from GizmoCommands import *

# /////////// Start Up, "Front End" /////////////
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
        # commented out code that doesn't seem to work. Docs said it should, but I dunno.
        # leaving it in there just in case, because we may need it later


@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print("Ready to roll!")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S"))

    # await client.change_presence(status=discord.Status.dnd, activity=discord.ActivityType.watching('Star Wars')) -- Alternatives,
    # You've gotta lot of options with these


# ///////////////// End "Front End" ///////////////////////

@bot.command()
async def dev(ctx):
    devEmbed = discord.Embed(title="Developers:",
                             description="**These peeps worked to bring me to me to what I am today:**\n"
                                         + "\nflop#2371\nSeltzer#0006\nklb#5169\n\n"
                                         + "**Version:**\t 0.0.0\n"
                                         + "**Date Released:** \t N/A", color=discord.Color.purple())

    await ctx.send(embed=devEmbed)
    # playing with embeds

@bot.command()
async def help(ctx):
    helpEmbed=discord.Embed(title="In your hour of need! Gizmo is here~", description="**Commands:**\n"+
                            "**^r** -> Roll some dice (Format 1d20)\n"+
                            "**^purge** -> Delete some messages (Format purge 3)\n"+
                            "**^choose** -> Gizmo will decide!\n(Format:^choose pizza burgers)\n" +
                            "**^speak** -> Gizmo will speak to you\n" +
                            "**^dev** -> See the Development Team/Version\n"+
                            "\n\n***Gizmo is still a kitten, let us know about any possible bugs!***", color=discord.Color.orange())
    await ctx.author.send(embed=helpEmbed)

# ////// Who's who: ///////
async def on_member_join(ctx, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await ctx.send(to_send)


@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please use proper formatting. Use ^help for more info.')


##[Start-Dice-Functions]##
@bot.command()
async def r(ctx, rolls: str):
    resultString,results,numDice = roll(rolls)
    await ctx.send(roll_str(rolls) + " for %s" % ctx.message.author.name)
    if resultString == '20':
        await ctx.send(ctx.author.mention + "  :game_die:\n**Critical Success!** " + resultString)
    elif resultString == '1':
        await ctx.send(ctx.author.mention + "  :game_die:\n**Critical Failure!** " + resultString)
    elif numDice == '1':
        await ctx.send(ctx.author.mention + "  :game_die:\n**Result:** " + resultString)
    else:
        await ctx.send(ctx.author.mention + "  :game_die:\n**Result:** " + resultString + "\n**Total:** " + str(results))

# outputs username + whole message after command
@bot.command()
async def cTest(ctx, *, arg):
    user = ctx.message.author
    formatUser = str(user)
    # gets rid of anything past # for example klb#5169 -> klb
    x = formatUser.index("#")
    formatUser = formatUser[0:x]

    testVar = discord.Embed(title="Member: " + str(formatUser) + " said: " + arg)
    await ctx.send(embed=testVar)

##}} Allows the users to call a command as such: ^roll 2 20 // will Return value of 2 D20 die {{##
@bot.command(pass_context=True)
async def d(ctx, die: int):
    results = []
    for role in range(1):
        x = random.randint(1, die)
        results.append(x)
        embedVar = discord.Embed(title="You rolled a D" + str(die), description="And you got " + str(results) + "!")
        embedVar.color = discord.Color.dark_gold()
        await ctx.send(embed=embedVar)


# d == old dice command
# roll == the dice command she tells you not to worry about
# keeping d for context
##===End-Dice-Commands==##

############## Purge #######################
@bot.command()
@commands.bot_has_permissions(administrator=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)
    await asyncio.sleep(2)
    await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention))
 

##^Just purges stuff pretty much
@purge.error  ##Simple error checking
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ha! You're not worthy!")


###------Gonna worry about this one later lol----------------------------------------

@bot.command()  # allows users to test the response of the bot from Discord
async def test(ctx):
    await ctx.send('Ready to roll!'.format(ctx.author))

@bot.command()
async def speak(ctx):
    meow = ['meow','Meow!','Meoooooow','mew','purrrrr','....','no','Mew!','Meow','Mew','purr']
    await ctx.send(random.choice(meow))

@bot.command()
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


# ///////////Test/////////////////////
# ////////////////////////////////////
@bot.command()  # shuts down the bot
async def stop(ctx):
    await ctx.send("Logging out. See you next session!".format(ctx.author))
    sys.exit()


@bot.command()
async def insult(ctx):
    """random insult"""
    lines = open('insults.txt').read().splitlines()
    await ctx.send(random.choice(lines))

bot.run('NzYzMjEyNzg0NzExMzY4NzE1.X30bSw.tp2tlQU4e8GdwvCGYtmHM1Xaalw')
