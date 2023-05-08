from Business.Conversions import convertToGrams
from Business.convertToText import readPicture


def startFunc():
    result = list()
    ingredients = readPicture('recipe3.jpg')
    for sentence in ingredients:
        result.append(convertToGrams(sentence))

    print(result)















if __name__ == '__main__':

    startFunc()



