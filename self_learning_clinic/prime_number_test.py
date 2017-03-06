import unittest
from prime_numbers import primenumbers

class Test_prime_numbers(unittest.Testcase):
	def test_returns_correct_primes(self):
		self.assertTrue(primenumbers(20), [1,3,5,7,11,13,17,19])

	def test_assert_input_is_not_string(self):
		self.assertRaises(TypeError, primenumbers('a_string'))

	def test_asserts_input_not_negative(self):
		self.assertIs(primenumbers(-5), 'Please don\'t input negatives')

	def test_returns_primes_in_array(self):
		# Result should be an array
		self.assertIsInstance(primenumbers(16), List)			
