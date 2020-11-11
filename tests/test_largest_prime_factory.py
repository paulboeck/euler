import unittest

from problems.largest_prime_factor import largest_prime_factor


class TestMultiplesOf3And5(unittest.TestCase):
    def test_largest_prime_factor(self):
        """
        Test that the code for 'Largest Prime Factor' returns the appropriate sum given an input
        :return:
        """
        self.assertEqual(29, largest_prime_factor(13195))
        self.assertEqual(6857, largest_prime_factor(600851475143))


if __name__ == '__main__':
    unittest.main()