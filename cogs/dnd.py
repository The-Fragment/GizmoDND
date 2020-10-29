import discord
from discord.ext import commands
from discord.ext.commands import bot
from GizmoCommands import *



class DnD(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @bot.command()
    async def r(self, ctx, rolls: str):
        resultString, results, numDice = roll(rolls)
        await ctx.send(roll_str(rolls) + " for %s" % ctx.message.author.name)
        if resultString == '20':
            await ctx.send(ctx.author.mention + "  :game_die:\n**Critical Success!** " + resultString)
        elif resultString == '1':
            await ctx.send(ctx.author.mention + "  :game_die:\n**Critical Failure!** " + resultString)
        elif numDice == '1':
            await ctx.send(ctx.author.mention + "  :game_die:\n**Result:** " + resultString)
        else:
            await ctx.send(
                ctx.author.mention + "  :game_die:\n**Result:** " + resultString + "\n**Total:** " + str(results))

    @bot.command()
    async def d(self, ctx, die: int):
        results = []
        for roll in range(1):
            x = random.randint(1, die)
            results.append(x)
            embed_var=discord.Embed(title="You rolled a D"
                                          + str(die), description="And you got: "
                                                                + str(results))
            embed_var.color=discord.Color.dark_gold()
            await ctx.send(embed=embed_var)
