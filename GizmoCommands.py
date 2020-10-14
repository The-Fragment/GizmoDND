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
from random import randint  # For use in dice rolling
import sys  # Safety feature for shutting down the bot, so I've read
from discord.utils import get
import time
import pip._internal.network
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



def do_magik(self, scale, *imgs):
		try:
			list_imgs = []
			exif = {}
			exif_msg = ''
			count = 0
			for img in imgs:
				i = wand.image.Image(file=img)
				i.format = 'jpg'
				i.alpha_channel = True
				if i.size >= (3000, 3000):
					return ':warning: `Image exceeds maximum resolution >= (3000, 3000).`', None
				exif.update({count:(k[5:], v) for k, v in i.metadata.items() if k.startswith('exif:')})
				count += 1
				i.transform(resize='800x800>')
				i.liquid_rescale(width=int(i.width * 0.5), height=int(i.height * 0.5), delta_x=int(0.5 * scale) if scale else 1, rigidity=0)
				i.liquid_rescale(width=int(i.width * 1.5), height=int(i.height * 1.5), delta_x=scale if scale else 2, rigidity=0)
				magikd = BytesIO()
				i.save(file=magikd)
				magikd.seek(0)
				list_imgs.append(magikd)
			if len(list_imgs) > 1:
				imgs = [PIL.Image.open(i).convert('RGBA') for i in list_imgs]
				min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
				imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
				imgs_comb = PIL.Image.fromarray(imgs_comb)
				ya = BytesIO()
				imgs_comb.save(ya, 'png')
				ya.seek(0)
			elif not len(list_imgs):
				return ':warning: **Command download function failed...**', None
			else:
				ya = list_imgs[0]
			for x in exif:
				if len(exif[x]) >= 2000:
					continue
				exif_msg += '**Exif data for image #{0}**\n'.format(str(x+1))+code.format(exif[x])
			else:
				if len(exif_msg) == 0:
					exif_msg = None
			return ya, exif_msg
		except Exception as e:
			return str(e), None