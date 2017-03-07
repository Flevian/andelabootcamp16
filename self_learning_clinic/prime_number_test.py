import unittest
""" import function primesnumbers from prime_numbers file in order to test it"""
from prime_numbers import primesnumbers

class Test_prime_numbers(unittest.TestCase):
	def test_returns_correct_primes(self):
		""" Output should be prime numbers only"""
		self.assertTrue(primesnumbers(25), [1, 3, 5, 7, 11, 13, 17, 19, 23])

	def test_assert_input_is_not_string(self):
		""" Input should be a an int"""
		self.assertRaises(TypeError, primesnumbers('a_string'))

	def test_asserts_input_not_negative(self):
		""" Input should be a positive value"""
		self.assertIsNot(primesnumbers(-5), 'Please don\'t input negatives')

	def test_returns_primes_in_array(self):
		""" Result should be an array"""
		self.assertIsInstance(primesnumbers(25), list)

	def test_asserts_input_not_zero(self):
		""" Input should be not be zero"""
		self.assertIsNot(primesnumbers(0), 'Zero is not prime number')		
	    
if __name__ == "__main__":
	unittest.main()

