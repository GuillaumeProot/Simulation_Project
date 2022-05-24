from collections import Counter
from chi2 import *
import numpy as np


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
    kr = chi2_test(list(count_of_gap_size.values()),
                                list(lr_prob.values()),
                                deg)
    # plt.bar(lengths.keys(), lengths.values())
    # plt.show()
    return kr
