from collections import Counter
import scipy as sc
from scipy.stats import chisquare
import numpy as np



def chisquare_test(values, probs):
    """
    values : [values]
    probs : values[i] has the probability probs[i] to happend
    """
    
    

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
        t = seq[:k]
        l = Counter(t)
        to_add = len(l)
        r.append(to_add)
        seq = seq[k:]
    # number_count is the number of time we got X different digits in a package
    # for exemple, we got in a package [1, 2, 2, 2, 5, 5]
    # we will have {3 : 1} meaning that there is one package where we got 3 different digits
    digits_count = Counter(r)
    r_tab = list(digits_count.values()) # values of digits_count
    poker_prob_tab = [poker_case_prob(k, r, d) for r in digits_count]
    # now return a chisquareTest of this
    dist, pvalue = chisquare(r_tab, poker_prob_tab)
    uni = "YES" if pvalue > 0.05 else "NO"
    print(f"{'Distance':^12} {'pvalue':^12} {'Uniform?':^8} {'Dataset'}")
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8} {r_tab}")
    
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
    
    
