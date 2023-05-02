import re
from DAL.ConversionTable import getAllIngredients, getWeightOfIngredientInUnit

# Sites to use:
# https://www.kingarthurbaking.com/learn/ingredient-weight-chart
# https://www.dovesfarm.co.uk/hints-&-tips/cups-to-grams-conversion-table
# https://www.carine.co.il/%D7%94%D7%9E%D7%A8%D7%AA-%D7%9E%D7%99%D7%93%D7%95%D7%AA-%D7%95%D7%9E%D7%A9%D7%A7%D7%9C%D7%95%D7%AA/
# https://www.allrecipes.com/article/cup-to-gram-conversions/


tbspList = ['tbsp', 'tablespoon']
tspList = ['tsp', 'teaspoon']
cupsList = ['cup', 'cups']
ounceList = ['ounce', 'oz']
keywords = tspList + tbspList + cupsList + ounceList

TSP = 1
TBSP = 2
CUP = 3
OZ = 4


def getUnitIndexInSentence(sentence, unit):
    searchIn = list()
    if unit == TBSP:
        searchIn = tbspList
    elif unit == TSP:
        searchIn = tspList
    elif unit == CUP:
        searchIn = cupsList
    elif unit == OZ:
        searchIn = ounceList

    for name in searchIn:
        try:
            index = sentence.index(name)
            if index != -1:
                return index
        except ValueError:
            index = -1

    return -1


def convertStringToNumber(sentence, unit):  ##
    p = '[-]?[0-9]+[,.]?[0-9]*([\\/][0-9]+[,.]?[0-9]*)*'
    #p = '[-]?[0-9]+[,.]?[0-9]*([\\/][0-9]+[,.]?[0-9]*)*([\\/ ][0-9]+[,.]?[0-9]*)*'    #the last part for 1 3/4


    # search before the UNIT in the sentence the number in string form!!
    # if unit is TSP than check before the word tsp in this sentence and get the number!
    # DO I really need to search before the unit? , maybe to cancel other numbers further ahead

    unitIndex = getUnitIndexInSentence(sentence, unit)
    if unitIndex == -1:
        return -1

    numberFound = re.search(p, sentence[:unitIndex])
    if numberFound is None:
        return -1

    numberFound = numberFound.string
    return convertToFloat(numberFound)


def gramsExists(sentence):
    if 'gram' in sentence:
        return True

    numbersFound = re.findall(r'\d+', sentence)
    sentencedWithoutSpace = sentence.replace(" ", "")  # if there is 400 g and not 400g
    for number in numbersFound:
        index = sentencedWithoutSpace.find(number)
        if index + 1 < len(sentencedWithoutSpace):
            if sentencedWithoutSpace[index + 1] == 'g':  # There is a number and than g, that means 400g
                return True
    return False


def getIngredientFromSentence(sentence):
    ingredients = getAllIngredients()

    foundList = list()  # put results to list if we have for example "flour" and "self-raising flour"
    for ingredient in ingredients:
        if ingredient in sentence:
            foundList.append(ingredient)

    if len(foundList) != 0:
        return max(foundList, key=len)  # returns the longest ingredient

    return ""  # found nothing!


def getAmountOfIngredientInGrams(ingredient, amount, unit):
    # result should be like this : "50g flour"

    weightOfUnit = getWeightOfIngredientInUnit(ingredient, unit)
    totalWeight = amount * weightOfUnit
    # return totalWeight + " g " + ingredient

    return "50g flour"


def convertUnitToGrams(sentence, unit):
    if gramsExists(sentence):
        return sentence

    # if there are no gram, search the number of the units we need to convert and convert it by the unit
    amount = convertStringToNumber(sentence, unit)

    ingredient = getIngredientFromSentence(sentence)

    if amount == -1 or ingredient == '':  # couldn't find number of ingredient in the sentence
        return sentence

    result = getAmountOfIngredientInGrams(ingredient, amount, unit)
    return result


def convertToGrams(sentence: str):
    currLower = sentence.lower()
    if any(a in currLower for a in tbspList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in tspList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in cupsList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in ounceList):
        return convertUnitToGrams(currLower, TBSP)
    else:
        return currLower  # No need to convert this sentence to grams


def convertToFloat(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))


# for tests!
def getNumOfUnit(unitString):
    if unitString == 'cup':
        return CUP
    elif unitString == 'tsp':
        return TSP
    elif unitString == 'tbsp':
        return TBSP
    elif unitString == 'oz':
        return OZ
    else:
        return -1


if __name__ == '__main__':
    print('Conversions')
