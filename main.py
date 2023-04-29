from Conversions import convertToGrams
from convertToText import readPicture


def startFunc():
    result = list()
    ingredients = readPicture('recipe1.jpg')
    for ingredient in ingredients:
        result.append(convertToGrams(ingredient))

    print(result)















if __name__ == '__main__':

    startFunc()



