from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import chisquare
import numpy as np
from chi2 import chi2_test

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


def poker_test(d, k):
    """
    seq : the sequence of number we want to test the uniformity
    d   : 
    """
    # cut the seq in package of size k
    r = []
    j = 0
    seq = get_pi_seq()
    while j+k < len(seq):       # this is the most efficient way to do it
        # count occurences in a package
        # add the number of different value to r
        r.append(len(Counter(seq[j:j+k])))
        j += k
    digits_count = Counter(r)   # count occurences of each value
    while j+k < len(seq):       # this is the most efficient way to do it
        # count occurences in a package
        # add the number of different value to r
        r.append(len(Counter(seq[j:j+k])))
        j += k
    digits_count = Counter(r)   # count occurences of each value
    r_tab = list(digits_count.values()) # poker value (pair, full, etc)
    poker_prob_tab = [poker_case_prob(k, r, d) for r in digits_count]

    # plot the repartition of the 'poker values'
    absiss = list(digits_count.keys())
    plt.title(f"Test de poker avec {k} splits")
    plt.xlabel("Nombre de digit différent par split")
    plt.ylabel("Nombre de splits")
    plt.bar(absiss, r_tab)
    plt.show()

    # Kr number
    degree = d-1
    kr = chi2_test(r_tab, poker_prob_tab, degree)
    print(f"Kr : {kr}")
    print(f"Degré de liberté : {degree}")
    

def get_pi_seq():
    file = open('pi.txt', "r")
    lines = file.readlines()[1:]
    clean_lines = [l.strip() for l in lines]
    str_line = "".join(clean_lines)
    return [int(x) for x in str_line]

def pi_chisquare_test():
    """
    do X² test on the decimals of pi
    """
    pi = get_pi_seq()
    dist, pvalue = chisquare(list(Counter(pi).values()))
    uni = "YES" if pvalue > 0.05 else "NO"
    print(f"{'Distance':^12} {'pvalue':^12} {'Uniform?':^8} {'Dataset'}")
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8} no")
