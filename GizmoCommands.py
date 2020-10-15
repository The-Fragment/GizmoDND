import json
import PIL
import numpy as np
from PIL import *
import discord
import asyncio, aiohttp
from discord.ext import commands  # Returns a warning, not sure why - // Commands
from discord.ext.commands import bot
import random
import wand
from io import *
import requests
from bs4 import BeautifulSoup
from random import randint  # For use in dice rolling
import sys  # Safety feature for shutting down the bot, so I've read
from discord.utils import get
import time
from imgurpython import ImgurClient

# Ex. takes in 2d20 and outputs the string Rolling 2 d20
def roll_str(rolls):
	numDice = rolls.split('d')[0]
	diceVal = rolls.split('d')[1]
	if numDice == '':
		numDice = int(1)
	return "Rolling %s d%s" % (numDice, diceVal)


# Ex. takes in 2d20 and outputs resultString = 11, 19 results = 30 numDice = 2
def roll(rolls):
	results = 0
	resultString = ''
	try:
		numDice = rolls.split('d')[0]
	except Exception as e:
		print(e)
		return "Use proper format!"
	rolls, limit = map(str, rolls.split('d'))
	if rolls == '':
		rolls = int(1)
	limit = int(limit)
	for r in range(rolls):
		number = random.randint(1, limit)
	results = results + number
	if resultString == '':
		resultString += str(number)
	else:
		resultString += ', ' + str(number)
# Returns 3 variables, make sure to store in 3 variables
	return resultString, results, numDice
