import math

import numpy as np

from generateur import open_file

py_numbers = np.array(list(open_file()))

class Generator1:
	
	
	def __init__(self, seed=0, nb_digits=10):
		self.seed = seed
		self.index = seed % len(py_numbers)
		self.nb_digits = nb_digits

	def random(self):
		digits = []
		for i in range(self.nb_digits):
			digit = py_numbers[self.index]
			digits.append(digit)
			self.index = (self.index + 1) % len(py_numbers)
		return float("0." + "".join(map(lambda x: str(x), digits)))

