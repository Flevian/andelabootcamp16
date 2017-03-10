class PrimeChecker(object):
	def is_prime(self, number):
		try:
			if number % 2 == 0:
				return False

			else:	
				if all(number % i != 0 for i in range(2, int(number**0.5 ) + 1)):
					if number < 2:
						return False
					else:
						return True

				else:
					return False 		
		except TypeError:
				return "invalid input"	  
  	      


prime = PrimeChecker()
print(prime.is_prime(number))	