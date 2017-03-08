def data_types(variablee):
	if isinstance(variable, str):
		return len(variable)

	elif isinstance(variable, bool):
		return ("Boolean")	

	elif isinstance(variable, int):
		if variable < 100:
			return "Less than 100"

		elif variable > 100:
			return "Greater than 100"
 
		else:
			return "Equal to 100"

	elif  isinstance(variable, list):
		return (variable[3])

	elif isnotinstance(variable, str):
		return "None"

	else:
		return "invalid input"
variable = 59 
print(data_types(variable))

