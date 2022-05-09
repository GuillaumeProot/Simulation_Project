from itertools import count
from operator import mul
from functools import reduce
from scipy.special import comb
import numpy as np
from collections import Counter
import math
import matplotlib.pyplot as plt


def computeStirling(k, r, pred={}):
    """
    find the stirling number {k r}.
    pred is a dictionary containing the previously computed (k, r) stirling number.
    """
    if (k, r) in pred:          # we already know it, don't recompute it
        return pred[(k, r)]
    if r == k or r == 1:        # base case
        return 1
    # compute the number for (k, r)
    pred[(k, r)] = computeStirling(k-1, r-1, pred=pred) + r * computeStirling(k-1, r)
    return pred[(k, r)]
    

def poker_case_prob(k, r, d):
    """
    return the probability of the poker test.
    
    k : size of packages
    r : used to generate r package of size k
    d : the number of possible different value (should be 10)
    """
    return (computeStirling(k, r) * np.prod([d-i for i in range(r)])) / (d**k)
    
def poker_test(seq, d, k):
    # cut the seq in package of size k
    r = []
    while len(seq) > 0:
        # count occurences in a package
        # add the number of different value to r
        r.append(len(count(seq[:k])))
        seq = seq[k:]
    # number_count is the number of time we got X different digits in a package
    # for exemple, we got in a package [1, 2, 2, 2, 5, 5]
    # we will have {3 : 1} meaning that there is one package where we got 3 different digits
    digits_count = count(r)
    r_tab = list(digits_count.values()) # values of digits_count
    poker_prob_tab = [poker_case_prob(k, r, d) for r in digits_count]
    # now return a chisquareTest of this
    
    
    
if __name__=="__main__":
    print("i'm main")
