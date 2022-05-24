from collections import Counter
from ctypes import ArgumentError
from chi2 import *
import numpy as np


def gap_test(seq, a=0, b=1/2, pi=False):
    if a > b:
        raise ArgumentError(f"Error : must have a < b!")
    b = 0.9 if (pi and b>0.9) else b
    p = np.floor(10*b)/10 - np.ceil(10*a)/10 + 0.1 if pi else b-a 
    gaps = []                   # len of all gaps
    gap_size = 0
    for val in seq:
        if (not pi and a <= val <= b) or (pi and a <= val/10 <= b):
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
    kr = chi2_test(list(count_of_gap_size.values()),
                                list(lr_prob.values()),
                                deg)
    # plt.bar(lengths.keys(), lengths.values())
    # plt.show()
    return kr
