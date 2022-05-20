import random
from generators import *
from matplotlib import pyplot as plt
import math
import numpy as np

def open_file():
    with open("pi.txt", "r") as pi:
        for line in pi:
            line = line.strip()
            if "." in line:
                line = line.split(".")[1]
            for c in line:
                yield int(c)




def kolmogorov_smirnov(numbers):
    numbers = np.sort(numbers)
    n = len(numbers)
    distance = np.max(np.array([np.abs((i/n)-numbers[i]) for i in range(len(numbers))]))
    critical = (1.358/math.sqrt(n))
    return distance < critical, distance, critical



if __name__ == '__main__':
    pyth_numbers = []
    for _ in range(2000):
        pyth_numbers.append(random.uniform(0,1))

    randomgen1 = Generator1(50)
    gen_numbers_1 = [randomgen1.random() for _ in range(2000)]

    print(gen_numbers_1)

    randomgen3 = Generator3()
    gen_numbers_3 = [randomgen3.random() for _ in range(2000)]

    print(gen_numbers_1)
    print("---------------------------------------")
    print(gen_numbers_3)

    print(f"Test de Kolmogorov-Smirnov pour notre générateur : \n"
        f"1 --> {kolmogorov_smirnov(gen_numbers_1)} \n"
        f"3 --> {kolmogorov_smirnov(gen_numbers_3)} \n"
        f"Python --> {kolmogorov_smirnov(pyth_numbers)}")

    
    plt.figure()
    plt.hist(gen_numbers_1, color='palegreen', histtype='barstacked')
    plt.hist(gen_numbers_3, color='gold', histtype='barstacked')
    plt.hist(pyth_numbers, color='darkblue', histtype='step')
    plt.legend({'Premier générateur', 'Python'}, loc=4)
    plt.savefig('generator1.png')
    plt.show()