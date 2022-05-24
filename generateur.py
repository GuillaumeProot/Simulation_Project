import random
from generators import *
from main import *
from scipy.stats import chisquare
from matplotlib import pyplot as plt
import math
import numpy as np
import datetime

def open_file():
    with open("pi.txt", "r") as pi:
        for line in pi:
            line = line.strip()
            if "." in line:
                line = line.split(".")[1]
            for c in line:
                yield int(c)


def gap_test(seq, a=0, b=1/2):
    p = b - a
    gaps = []                   # len of all gaps
    gap_size = 0
    for val in seq:
        if a <= val <= b:
            gaps.append(gap_size if gap_size < 10 else 10)
            gap_size = 0
        else:
            gap_size += 1
    count_of_gap_size = Counter(gaps) # count the occurence of each gap size
    # now we compute the proba for each gap size to happen
    lr_prob = {}
    for size in count_of_gap_size.keys():
        if size < 10:
            lr_prob[size] = np.power(1-p, size)*p
        else:
            lr_prob[10] = np.power(1-p, size+1)
    
    deg = len(lr_prob)-1
    kr = compute_kr(list(count_of_gap_size.values()),
                                list(lr_prob.values()),
                                deg)
    # plt.bar(lengths.keys(), lengths.values())
    # plt.show()
    return kr

   

def kolmogorov_smirnov_uniform_test(numbers):
    """
    Kolmogorov-Smirnov test for uniform distribution
    """
    size = len(numbers)
    # get the cdf of the sample
    sample_cdf = np.cumsum(numbers) / size
    # get the cdf of the uniform distribution
    uniform_cdf = np.arange(size) / size
    # get the distance between the two cdf
    d = np.max(np.abs(sample_cdf - uniform_cdf))
    # get the critical value
    critical_value = math.sqrt(1.36 * (1 / 2000))
    # test if the distance is greater than the critical value
    if d > critical_value:
        return "The sample is not uniformly distributed"
    else:
        return "The sample is uniformly distributed"


if __name__ == '__main__':
    pyth_numbers = []
    for _ in range(2000):
        pyth_numbers.append(random.uniform(0,1))

    randomgen1 = Generator1(50)
    gen_numbers_1 = [randomgen1.random() for _ in range(2000)]

    # print(gen_numbers_1)
    # print("---------------------------------------")

    randomgen2 = Generator2()
    gen_numbers_2 = [randomgen2.random() for _ in range(2000)]

    # print(gen_numbers_2)
    # print("---------------------------------------")

    randomgen3 = Generator3()
    gen_numbers_3 = [randomgen3.random() for _ in range(2000)]
    
    
    # print(gen_numbers_3)
    # print("---------------------------------------")
    
    randomgen4 = Generator4()
    gen_numbers_4 = [randomgen4.random() for _ in range(2000)]
    
    # print(gen_numbers_4)
    # print("---------------------------------------")
    
    print(f"Test de Kolmogorov-Smirnov pour notre générateur : \n"
        f"1      --> {kolmogorov_smirnov_uniform_test(gen_numbers_1)} \n"
        f"2      --> {kolmogorov_smirnov_uniform_test(gen_numbers_2)} \n"
        f"3      --> {kolmogorov_smirnov_uniform_test(gen_numbers_3)} \n"
        f"4      --> {kolmogorov_smirnov_uniform_test(gen_numbers_4)} \n"
        f"Python --> {kolmogorov_smirnov_uniform_test(pyth_numbers)}")

    
    print(f"Test de gap pour notre générateur :")
    print(f"1      -------")
    gap_test(gen_numbers_1)
    print("-------")
    print(f"2      -------")
    gap_test(gen_numbers_2)
    print("-------")
    print(f"3      -------")
    gap_test(gen_numbers_3)
    print("-------")
    print(f"4      -------")
    gap_test(gen_numbers_4)
    print("-------")
    print(f"python -------")
    gap_test(pyth_numbers)
    print("-------")
    
    # plt.figure()
    # plt.hist(gen_numbers_1, color='palegreen', histtype='barstacked')
    # plt.hist(pyth_numbers, color='darkblue', histtype='step')
    # plt.legend({'Premier générateur','Python'}, loc=4)
    # plt.savefig('generator1.png')
    # plt.show()

    # plt.figure()
    # plt.hist(gen_numbers_2, color='palegreen', histtype='barstacked')
    # plt.hist(pyth_numbers, color='darkblue', histtype='step')
    # plt.legend({'deuxième générateur','Python'}, loc=4)
    # plt.savefig('generator2.png')
    # plt.show()

    # plt.figure()
    # plt.hist(gen_numbers_3, color='gold', histtype='barstacked')
    # plt.hist(pyth_numbers, color='darkblue', histtype='step')
    # plt.legend({'Troisième générateur','Python'}, loc=4)
    # plt.savefig('generator3.png')
    # plt.show()

    # plt.figure()
    # plt.hist(gen_numbers_4, color='paleblue', histtype='barstacked')
    # plt.hist(pyth_numbers, color='darkblue', histtype='step')
    # plt.legend({'Quatrième générateur','Python'}, loc=4)
    # plt.savefig('generator4.png')
    # plt.show()
