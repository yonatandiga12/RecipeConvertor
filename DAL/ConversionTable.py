ingredientsList = list()


# return all the ingredients saved in the conversion table!
def getAllIngredients():
    # it checks if we pulled it already to memory for fewer I/O operations.
    if len(ingredientsList) != 0:
        return ingredientsList

    # ingredientsList = getFromDB()  but do lower to all of them!!

    return ['flour', 'salt', 'water']  # temp


# return the amount in grams of this ingredient in this unit, for example: "flour", "tbsp" should return 9
def getWeightOfIngredientInUnit(ingredient, unit):

    #go to ingredient and return the correct unit

    return 100







