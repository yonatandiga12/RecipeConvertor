import unittest
from unittest import TestCase
from Business.Conversions import convertStringToNumber, gramsExists, getIngredientFromSentence, getNumOfUnit


class TestConversions(TestCase):


    def test_convertStringToNumber_Valid(self):
        result = convertStringToNumber("1 1/2 cup milk", getNumOfUnit('cup'))
        self.assertEqual(result, 1.5)

        result = convertStringToNumber("5/2 tbsp milk", getNumOfUnit('tbsp'))
        self.assertEqual(result, 2.5)

        result = convertStringToNumber("1 cup milk", getNumOfUnit('cup'))
        self.assertEqual(result, 1)

        result = convertStringToNumber("1.5 cup milk", getNumOfUnit('cup'))
        self.assertEqual(result, 1.5)

        result = convertStringToNumber("0.5 cup milk", getNumOfUnit('cup'))
        self.assertEqual(result, 0.5)


        result = convertStringToNumber("1/3 cup milk", getNumOfUnit('cup'))
        self.assertEqual(result, 1/3)

        result = convertStringToNumber("10 tablespoons (145 grams) unsalted butter", getNumOfUnit('tbsp'))
        self.assertEqual(result, 10)


    def test_convertStringToNumber_ShouldFail(self):

        result = convertStringToNumber("1 large egg", getNumOfUnit('cup'))
        self.assertEqual(result, -1)

        result = convertStringToNumber("1 tbsp flour", getNumOfUnit('cup'))
        self.assertEqual(result, -1)

        result = convertStringToNumber("1 cup flour", getNumOfUnit('tsp'))
        self.assertEqual(result, -1)

        result = convertStringToNumber("1 tsp flour", getNumOfUnit('tbsp'))
        self.assertEqual(result, -1)

        result = convertStringToNumber("85g plain flour", getNumOfUnit('tbsp'))
        self.assertEqual(result, -1)





    def test_gramsExists(self):
        self.fail()


    def test_getIngredientFromSentence(self):
        self.fail()



if __name__ == '__main__':
    unittest.main()



