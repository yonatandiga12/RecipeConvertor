


#Sites to use:
#https://www.kingarthurbaking.com/learn/ingredient-weight-chart
#https://www.dovesfarm.co.uk/hints-&-tips/cups-to-grams-conversion-table
#https://www.carine.co.il/%D7%94%D7%9E%D7%A8%D7%AA-%D7%9E%D7%99%D7%93%D7%95%D7%AA-%D7%95%D7%9E%D7%A9%D7%A7%D7%9C%D7%95%D7%AA/
#https://www.allrecipes.com/article/cup-to-gram-conversions/


tbspList = ['tbsp', 'tablespoon']
tspList = ['tsp', 'teaspoon']
cupsList = ['cup', 'cups']
ounceList = ['ounce', 'oz']
keywords = tspList + tbspList + cupsList + ounceList

TSP = 1
TBSP = 2
CUP = 3
OZ = 4


def convertStringToNumber(sentence, unit):
    #search before the UNIT in the sentence the number in string form!!
    # if unit is TSP than check before the word tsp in this sentence and get the number!
    # if the number is fraction with / use the function below convert_to_float
    #                           with . do another function to get the float number
    return 1


def gramsExists(sentence):
    # Search if there are grams in this sentence, if there are return as is
    pass


def getIngredientFromSentence(sentence):
    #figure out what the ingredient is from the sentence and return a string of it.
    #maybe use some kind of DB of ingredients and check there for matches?
    #Maybe use the conversion table and check for ingredients listing in there? because only then we can convert them
    return ""


def getAmountOfIngredientInGrams(ingredient, amount, unit):
    #result should be like this : "50g flour"
    return  "50g flour"


def convertUnitToGrams(sentence, unit):
    if gramsExists(sentence):
        return sentence

    #if there are no gram, search the number of the units we need to convert and convert it by the unit
    amount = convertStringToNumber(sentence, unit)

    ingredient = getIngredientFromSentence(sentence)

    #calculate with the csv and the float we found how much is the ingredient in metric.
    result = getAmountOfIngredientInGrams(ingredient, amount, unit)
    #example: flour, 2.5, TBSP should be calculated by going to the csv and check for TBSP of flour and multiply by 2.5

    pass


def convertToGrams(ingredient: str):
    currLower = ingredient.lower()
    if any(a in currLower for a in tbspList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in tspList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in cupsList):
        return convertUnitToGrams(currLower, TBSP)
    elif any(a in currLower for a in ounceList):
        return convertUnitToGrams(currLower, TBSP)
    else:
        return currLower  #No need to convert this sentence to grams






def convert_to_float(frac_str):
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


if __name__ == '__main__':
    print('Conversions')


