from collections import Counter
from ctypes import ArgumentError
from chi2 import *
import numpy as np
import matplotlib.pyplot as plt

def gap_test(seq, a=0, b=1/2, pi=False):
    if a > b:
        raise ArgumentError(f"Error : must have a < b!")
    b = 0.9 if (pi and b>0.9) else b
    p = np.floor(10*b)/10 - np.ceil(10*a)/10 + 0.1 if pi else b-a 
    gap_size = 0
    gap_lengths = {}
    lr_probs = []
    for val in seq:
        if (not pi and a <= val <= b) or (pi and a <= val/10 <= b):
            if gap_size in gap_lengths:
                gap_lengths[gap_size] += 1
            else:
                gap_lengths[gap_size] = 1
                if gap_size >= 11:
                    lr_probs.append(np.power((1-p), 11))
                else:
                    lr_probs.append(p * np.power((1-p), gap_size))
            gap_size = 0
        else:
            gap_size = min(gap_size+1, 11) # if we go beyond 11, we regroup it
            # why ? Because the probability becomes really small
            
    kr = chi2_test(list(gap_lengths.values()), lr_probs)
    plt.bar(gap_lengths.keys(), gap_lengths.values())
    plt.show()
    return kr
