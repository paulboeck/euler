import unittest

from problems.multiples_3_and_5 import MultiplesOf3And5


class TestMultiplesOf3And5(unittest.TestCase):
    def test_multiples_of_3_and_5(self):
        """
        Test that the code for 'Multples of 3 and 5' returns the appropriate sum given an input
        :return:
        """
        self.assertEqual(23, MultiplesOf3And5.sum_multiples_of_3_and_5(10))
        self.assertEqual(233168, MultiplesOf3And5.sum_multiples_of_3_and_5(1000))
        # Included this test during development to try to find the fastest algorithm
        #self.assertEqual(233168, MultiplesOf3And5.sum_multiples_of_3_and_5(100000000))


if __name__ == '__main__':
    unittest.main()
