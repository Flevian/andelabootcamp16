class Student(object):
	"""This is a Superclass
       It holds holds the total number of students
	"""
	counter = 0

	def __init__(self):
		type(self).counter += 1

	def __del__(self):
		type(self).counter -= 1	

	def student_stream(self):
		"""data encapsulation: color can not be accessed by another class
		Abstraction: checks the color if it valid
		"""
		if self._color == "yelow":
			stream = "North"

		elif self._color == "pink":
			strem = "South"

		elif self._color == "red":
			stream = "East"

		else:
			stream = "Invalid stream"

		return stream	


class Students(Student):
	"""Subclass of Student_counter: it inherits methods from Student_counter
       It holds student details
	"""
	def __init__(self, name, school_id, fees_paid, student_class, color):
		self.name = name
		self.school_id = school_id
		self.fees_paid = fees_paid
		self.student_class = student_class
		self._color = color

		Student.__init__(self)

		if self.student_class == 4:
			self.__fees = 5000

		elif student_class == 3:
			self.__fees = 4000

		elif student_class == 2:
			self.__fees = 37122

		else:
			self.__fees = 56000					

	def fees_arrears(self):
		balance = self.__fees - self.fees_paid
		return balance 	



class Studentsubjects(Student):
	"""Subclass of Student_counter: it inherits methods from Student_counter
       It holds student details
	"""
	def __init__(self, name, color):
		self.name = name
		self._color = color

		Student.__init__(self)

		
	def student_stream(self):
		"""data encapsulation: color can not be accessed by another class
		Abstraction: checks the color if it valid
		Polymophism: using the same method to return different outputs
		"""
		if self._color == "yelow":
			stream = "Geography"

		elif self._color == "pink":
			stream = "Music"

		elif self._color == "red":
			stream = "Agriculture"

		else:
			stream = "Invalid stream"

		return stream		
   

