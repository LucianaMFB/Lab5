import unittest
from bubbleSort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_CP1(self):
        valores = [5]

        bubble_sort(valores)

        self.assertEqual(valores, [5])


    def test_CP2(self):
        valores = [1, 2]

        bubble_sort(valores)

        self.assertEqual(valores, [1, 2])


    def test_CP3(self):
        valores = [2, 1]

        bubble_sort(valores)

        self.assertEqual(valores, [1, 2])


    def test_CP4(self):
        valores = [1, 2, 3]

        bubble_sort(valores)

        self.assertEqual(valores, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()