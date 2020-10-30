import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from GizmoCommands import *

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.Command()
    async def text(self, ctx, name, category: discord.CategoryChannel = None):
        guild = ctx.guild
        await guild.create_text_channel(name=name, category=category)
        await ctx.send(f'Created text channel `{name}`')

    @bot.Command()
    async def voice(self, ctx, name, category: discord.CategoryChannel = None):
        guild = ctx.guild
        await guild.create_voice_channel(name=name, category=category)
        await ctx.send(f'Created voice channel `{name}`')

    @bot.Command()
    @commands.has_guild_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await asyncio.sleep(2)
        await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention))

    ##^Just purges stuff pretty much
    @purge.error  ##Simple error checking
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Ha! You're not worthy!")

    @bot.Command()
    @commands.is_owner()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        timestamp = ctx.message.created_at.__format__('%A | %B %d, %I:%M %p UTC')
        embed = discord.Embed(
            color=0xff0000

        )
        embed.add_field(name=f"Kicked",
                        value=f"**❯ User:** {member.mention}\n**❯ Guild:** {member.guild.name}\n**❯ Kicked At:** {timestamp}",
                        inline=False)

        await ctx.send(embed=embed, delete_after=60)


def setup(bot):
    bot.add_cog(AdminCog(bot))
