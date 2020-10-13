import random
#from google_images_search import GoogleImagesSearch
from random import randint  # For use in dice rolling


# Ex. takes in 2d20 and outputs the string Rolling 2 d20
def roll_str(rolls):
    try:
        numDice = rolls.split('d')[0]
        diceVal = rolls.split('d')[1]
    except Exception as e:
        print(e)
        return "Use proper format!"
    return "Rolling %s d%s" % (numDice, diceVal)


# Ex. takes in 2d20 and outputs resultString = 11, 19 results = 30 numDice = 2
def roll(rolls):
    results = 0
    resultString = ''
    try:
        try:
            numDice = rolls.split('d')[0]
        except Exception as e:
            print(e)
            return "Use proper format!"
        rolls, limit = map(int, rolls.split('d'))
        for r in range(rolls):
            number = random.randint(1, limit)
            results = results + number
            if resultString == '':
                resultString += str(number)
            else:
                resultString += ', ' + str(number)
        # Returns 3 variables, make sure to store in 3 variables
        return resultString, results, numDice

    except Exception as e:
        print(e)
        return


########Bro I don't even know -- I'll leave it here tho###################
#def google(p):
#    jizz = GoogleImagesSearch('e7c7909e6de751939ee28f1c21bcd3bf305aac67', '8a163295e50d6d19c')
#    _search_params = {'q': '...',
#                  'num': 10,
#                  'safe': 'high|medium|off|',
#                  'fileType': 'jpg|gif|png',
#                  'imgType': 'clipart|face|lineart|news|photo',
#                  'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
#                  'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
#                  'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'}
#    jizz(_search_params=_search_params)
## this will search and download:
#    jizz(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
    jizz(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
    jizz(search_params=_search_params)
    for image in jizz.results():
        image.download('/path/')
        image.resize(500, 500)
