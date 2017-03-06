import unittest
from prime_numbers import primenumbers

class Test_prime_numbers(unittest.Testcase):
	def test_returns_correct_primes(self):
		self.assertTrue(primenumbers(20),[1,3,5,7,11,13,17,19]) 	
