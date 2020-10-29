import asyncio
import sys
import discord
from discord.ext import commands
from discord.ext.commands import bot
from GizmoCommands import *


class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
async def dev(self, ctx):
    devEmbed = discord.Embed(title="Developers:",
                             description="**These peeps worked to bring me to me to what I am today:**\n"
                                         + "\nflop#2371\nSeltzer#0006\nklb#5169\n\n"
                                         + "**Version:**\t 0.0.0\n"
                                         + "**Date Released:** \t N/A", color=discord.Color.purple())

    await ctx.send(embed=devEmbed)
    # playing with embeds


@bot.command()
async def help(self, ctx):
    helpEmbed = discord.Embed(title="In your hour of need! Gizmo is here~",
                              description="**Commands:**\n" +
                                          "**^r** -> Roll some dice (Format 1d20)\n" +
                                          "**^purge** -> Delete some messages (Format purge 3)\n" +
                                          "**^choose** -> Gizmo will decide!\n(Format:^choose pizza burgers)\n" +
                                          "**^speak** -> Gizmo will speak to you\n" +
                                          "**^dev** -> See the Development Team/Version\n" +
                                          "\n\n***Gizmo is still a kitten, let us know about any possible bugs!***",
                              color=discord.Color.orange())
    await ctx.author.send(embed=helpEmbed)


@bot.command()
async def joined(self, ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


# ////// Who's who: ///////
# async def on_member_join(ctx, member):
#     guild = member.guild
#     if guild.system_channel is not None:
#         to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
#         await ctx.send(to_send)
#
#
# @bot.event
# async def on_command_error(error, ctx):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please use proper formatting. Use ^help for more info.')
#


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
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="Emperor's New Groove"))
        await asyncio.sleep(45)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Among Us"))
        await asyncio.sleep(45)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Beat Saber"))
        await asyncio.sleep(45)


""" outputs username + whole message after command """


@bot.command()
async def cTest(self, ctx, *, arg):
    user = ctx.message.author
    formatUser = str(user)
    # gets rid of anything past # for example klb#5169 -> klb
    x = formatUser.index("#")
    formatUser = formatUser[0:x]
    testVar = discord.Embed(title="Member: " + str(formatUser) + " said: " + arg)
    await ctx.send(embed=testVar)


@bot.command()  # allows users to test the response of the bot from Discord
async def test(ctx):
    await ctx.send('Ready to roll!'.format(ctx.author))


@bot.command()  # shuts down the bot
async def stop(ctx):
    await ctx.send("Logging out. See you next session!".format(ctx.author))
    sys.exit()


def setup(bot):
    bot.add_cog(UtilityCog(bot))
