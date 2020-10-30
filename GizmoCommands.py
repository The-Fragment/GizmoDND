import random


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
    rolls = int(rolls)
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
