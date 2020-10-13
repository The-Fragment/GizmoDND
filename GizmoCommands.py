import random
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
        return resultString,results,numDice

    except Exception as e:
        print(e)
        return