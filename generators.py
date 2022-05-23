import math
import datetime
import numpy as np

import string
import random

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

class Generator2:

    def __init__(self, nb_digits=10):
        
        self.nb_digits = nb_digits


    def random(self):
        digits = []

        for _ in range(self.nb_digits):

            length_of_string = Generator3(7).random() * 1000000
            text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        
            asc = map(chr, text)
            index = (sum(asc) % 1000000)

            digit_result = py_numbers[int(index)] #selectionne le digit dans les decimales de pi a l'index index
            digits.append(digit_result)
        return float("0." + "".join(map(lambda x: str(x), digits)))


class Generator3:
    
    def __init__(self, nb_digits=10):
        self.nb_digits = nb_digits


    def random(self):
        digits = []

        for _ in range(self.nb_digits):
            nb_random = int(Generator1(50,6).random() * 100000)
            timing = datetime.datetime.now().microsecond #prend la date en microseconde
            digit = (timing*nb_random)%(2**32)
            index = (digit/(2**32)) * 1000000
        
            digit_result = py_numbers[int(index)] #selectionne le digit dans les decimales de pi a l'index index
            digits.append(digit_result)
        return float("0." + "".join(map(lambda x: str(x), digits)))