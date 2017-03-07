import unittest
""" import function primesnumbers from prime_numbers file in order to test it"""
from prime_numbers import primesnumbers

class Test_prime_numbers(unittest.TestCase):
	def test_returns_correct_primes(self):
		""" Output should be prime numbers only"""
		self.assertTrue(primesnumbers(25), [1, 3, 5, 7, 11, 13, 17, 19, 23])

	
	    
if __name__ == "__main__":
	unittest.main()

