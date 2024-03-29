import math
import datetime
import numpy as np
import time
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
        for i in range(self.nb_digits):
            time.sleep(1E-6)
            timing = datetime.datetime.now().microsecond # takes the date in microseconds
            digit = (timing*424242)%(2**32)
            index = (digit/(2**32)) * 1000000
        
            digit_result = py_numbers[int(index)] # selects the digit in the decimals of pi at the index
            digits.append(digit_result)
        return float("0." + "".join(map(lambda x: str(x), digits)))


class Generator3:

    def __init__(self, nb_digits=10):
        
        self.nb_digits = nb_digits


    def random(self):
        digits = []

        for _ in range(self.nb_digits):

            length_of_string = Generator1(50,3).random() * 1000
            text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(int(length_of_string)))
            
            asc = [ord(c) for c in text]

            index = (sum(asc) % 1000000)

            digit_result = py_numbers[int(index)] # selects the digit in the decimals of pi at the index
            digits.append(digit_result)
        return float("0." + "".join(map(lambda x: str(x), digits)))


class Generator4:
    
    def __init__(self, nb_digits=10):
        self.nb_digits = nb_digits

    def random(self):
        digits = []

        for i in range(self.nb_digits):
            seed = datetime.datetime.now().microsecond
            index = self.hash(seed, i) % len(py_numbers)
            digits.append(py_numbers[index])
        return float("0." + "".join(map(lambda x: str(x), digits)))

    def hash(self, seed, i, c1=3, c2=5, m=3079):
        return (self.first_hash(seed) + c1*i + c2*np.power(i, 2)) % m
    
    def first_hash(self, seed, m=1543):
        return seed % m
