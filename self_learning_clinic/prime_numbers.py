def primesnumbers(number):
    prime_number_list = list()

    try:
    	if number < 2:
    		return False

    	for num in range(number+1):
    		"""Get the numbers that are only divisible by its self"""
        	if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
        		if num < 2:
        			pass
        		else:
        			prime_number_list.append(num)
    	return (prime_number_list)  
    except TypeError:
    	"invalid input"	  
  	      