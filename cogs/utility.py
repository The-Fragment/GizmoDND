import sys
import discord
from discord.ext import commands
from discord.ext.commands import bot
intents = discord.Intents.default()
intents.members = True


class UtilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@commands.command()
async def dev(self, ctx):
    devEmbed = discord.Embed(title="Developers:",
                             description="**These peeps worked to bring me to me to what I am today:**\n"
                                         + "\nflop#2371\nSeltzer#0006\nklb#5169\n\n"
                                         + "**Version:**\t 0.0.0\n"
                                         + "**Date Released:** \t N/A", color=discord.Color.purple())

    await ctx.send(embed=devEmbed)
    # playing with embeds


@commands.command()
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


@bot.Command()
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

""" outputs username + whole message after command """


@bot.Command()
async def cTest(self, ctx, *, arg):
    user = ctx.message.author
    formatUser = str(user)
    # gets rid of anything past # for example klb#5169 -> klb
    x = formatUser.index("#")
    formatUser = formatUser[0:x]
    testVar = discord.Embed(title="Member: " + str(formatUser) + " said: " + arg)
    await ctx.send(embed=testVar)


@bot.Command()  # allows users to test the response of the bot from Discord
async def test(ctx):
    await ctx.send('Ready to roll!'.format(ctx.author))


@bot.Command()  # shuts down the bot
async def stop(ctx):
    await ctx.send("Logging out. See you next session!".format(ctx.author))
    sys.exit()


def setup(bot):
    bot.add_cog(UtilityCog(bot))
