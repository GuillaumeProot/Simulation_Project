from collections import Counter
from math import sqrt
import matplotlib.pyplot as plt
import scipy as sc
from scipy.stats import chisquare
from scipy.stats import chi2
import numpy as np
    

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
    
def count(tab):
    c = {}
    for x in tab:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    return c

def poker_test(seq, d, k):
    # cut the seq in package of size k
    r = []
    j = 0
    while j+k < len(seq):       # this is the most efficient way to do it
        # count occurences in a package
        # add the number of different value to r
        r.append(len(count(seq[j:j+k])))
        j += k
    digits_count = count(r)   # count occurences of each value
    r_tab = list(digits_count.values()) # poker value (pair, full, etc)
    poker_prob_tab = [poker_case_prob(k, r, d) for r in digits_count]

    # plot the repartition of the 'poker values'
    absiss = list(digits_count.keys())
    plt.title(f"Poker test with {k} splits")
    plt.xlabel("Number of different digits by splits")
    plt.ylabel("Number of splits")
    plt.bar(absiss, r_tab)
    plt.show()

    # Kr number
    kr = compute_kr(r_tab, poker_prob_tab)
    print(f"Kr : {kr}")
    degree = d-1
    # TODO : help, I don't know what to trust here
    print(f"Freedom degree : {degree}")
    pvalues = {"0.1" : 14.684,
               "0.05" : 16.919,
               "0.01" : 21.666,
               "0.001" : 27.877}
    print("HYPOTHESIS : digits of pi are uniformly distributed")
    [print(f"ACCEPT with a pvalue of {pval}") if kr <= pvalues[pval] else print(f"REJECT with a pvalue of {pval}") for pval in pvalues.keys()]
    p = chi2.cdf(kr, df=d-1)
    print(f"pvalue : {chi2.cdf(kr, df=degree)}")
    [print(f"ACCEPT at {pval}") if p < 1-float(pval) else print(f"REJECT at {1-float(pval)}") for pval in pvalues.keys()]
    

def compute_kr(values, expected):
    Np = np.multiply(expected, np.sum(values))
    return np.sum(np.divide(np.power(np.subtract(values, Np), 2), Np))

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

if __name__=="__main__":
    print("i'm main")
    k = int(input("enter number of packets : "))
    poker_test(get_pi_seq(), 10, k)
    # print(computeStirling(100, 10))
    # pi_chisquare_test()
