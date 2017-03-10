def reverse_string(my_string):
	if type(my_string) == str:
		if len(my_string) == 0:
			return None
		else:	
			string_list = []

			for ch in my_string:
				string_list.append(ch)

			string_list.reverse()
			reversed_string = "".join(string_list)

			if my_string == reversed_string:
				return True

			else:
				return reversed_string	

	else: 
		return "invalid input, enter a string"	


my_string = "NaN"
print(reverse_string(my_string))		