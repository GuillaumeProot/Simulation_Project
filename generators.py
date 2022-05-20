import math
import datetime
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

class Generator2:

    def __init__(self, seed=0, nb_digits=10):
        self.seed = seed
        self.index = seed % len(e_numbers)
        self.nb_digits = nb_digits

    def random(self):
        digits = []
        for j in range(3):
            digit = []
            for k in range(self.nb_digits):
                digit2 = py_numbers[self.index]
                digit.append(digit2)
                self.index = (self.index + 1) % len(e_numbers)
            digits.append(float("0." + "".join(map(lambda x: str(x), digit))))
        return math.sqrt(sum([x ** 2 for x in digit])) / math.sqrt(3)

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