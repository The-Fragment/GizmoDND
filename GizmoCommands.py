import random
from random import randint  # For use in dice rolling

def roll_str(rolls):
    try:
        numDice = rolls.split('d')[0]
        diceVal = rolls.split('d')[1]
    except Exception as e:
        print(e)
        return "Use proper format!"
    return "Rolling %s d%s" % (numDice, diceVal)

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
        return resultString,results,numDice

    except Exception as e:
        print(e)
        return