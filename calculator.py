# Implements basic arithmetic operations and provides users with a simple calculator interface for performing calculations.
class calculator:

	import math

	def add(self, x, y):
		return x + y

	def subtract(self, x, y):
		return x - y

	def multiply(self, x, y):
		return x * y

	def divide(self, x, y):
		if y == 0:
			return "Error! division by zero"
		return x / y

	def power(self, x , y):
		return pow(x,y)

	def square(self, x):
		return self.math.sqrt(x)