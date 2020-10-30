import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext.commands import bot
from GizmoCommands import *

bot = commands.Bot(command_prefix='^')
intents = discord.Intents.default()
intents.members = True


class FunCog(commands.Cog):
    def __init__(self):
        self.bot = bot

    @bot.command()
    async def speak(self, ctx):
        meow = ['meow', 'Meow!', 'Meoooooow', 'mew', 'purrrrr', '....', 'no', 'Mew!', 'Meow', 'Mew', 'purr']
        await ctx.send(random.choice(meow))

    @bot.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @bot.Command()
    async def insult(self, ctx):
        """random insult"""
        lines = open('../insults.txt').read().splitlines()
        await ctx.send(random.choice(lines))

    @bot.Command()
    async def cursed(self, ctx):
        fp = 'images/'
        await ctx.send(file=discord.File(fp + 'cursed-images-beans-6.jpg'))

    @bot.Command()
    async def blessed(self, ctx):
        fp = 'images/'
        await ctx.send(file=discord.File(fp + 'blessed.jpg'))

    @bot.Command()
    async def compliment(self, ctx):
        """random compliment"""
        comp = open('../compliment.txt').read().splitlines()
        await ctx.send(random.choice(comp))

    @bot.Command()
    async def googy(self, ctx, *text: str):
        """LMGTFY search"""
        await ctx.send('http://lmgtfy.com/?q=' + '+'.join(text))

    @bot.Command()
    async def cat(self, ctx):
        await ctx.send("Enjoy a random cat!")
        source = requests.get('http://theoldreader.com/kittens/600/400/js').text
        soup = BeautifulSoup(source, 'lxml')
        img = soup.find('img')
        rcurl = "http://theoldreader.com" + str(img['src'])
        e = discord.Embed()
        e.set_image(url=rcurl)
        await ctx.send(embed=e)

    @bot.Command()
    async def src(self, ctx, *text: str):
        """Search google and embed results, WIP"""
        beanEmbed = discord.Embed(title='Your Search:', description=('Here ->'),
                                  url="https://google.com/search?q=" + "+".join(text))
        await ctx.send(embed=beanEmbed)

    def setup(self):
        self.add_cog(FunCog(self))
