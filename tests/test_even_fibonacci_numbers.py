import unittest

from problems.even_fibonacci_numbers import sum_even_fibonacci_terms


class TestEvenFibonacciNumbers(unittest.TestCase):
    def test_sum_even_fibonacci_terms(self):
        """
        Test that the code for 'Even Fibonacci numbers' returns the appropriate sum given an input
        :return:
        """
        self.assertEqual(10, sum_even_fibonacci_terms(10))
        self.assertEqual(44, sum_even_fibonacci_terms(100))
        self.assertEqual(36361730124070, sum_even_fibonacci_terms(40000000000000))


if __name__ == '__main__':
    unittest.main()
