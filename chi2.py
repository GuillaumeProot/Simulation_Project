import numpy as np
from scipy.stats import chi2

def chi2_test(values, expected, df=None, pvalues=[0.1, 0.05, 0.01, 0.001]):
    df = len(values)-1 if df == None else df
    Np = np.multiply(expected, np.sum(values))
    Kr = np.sum(np.divide(np.power(np.subtract(values, Np), 2), Np))
    [print(f"ACCEPT at {p : <6}% | {Kr : ^6.5f} <= {chi2.ppf(q=1-p, df=df) : ^7.5f} | df = {df}") if Kr <= chi2.ppf(q=1-p, df=df) else print(f"REJECT at {p : < 6}% | {Kr : ^6.5f} <= {chi2.ppf(q=1-p, df=df) : ^7.5f} | df = {df}") for p in pvalues]
    # NOTE :
    # HO : we are not uniform
    # if ACCEPT:
    # it means that we have p% of chance not to be uniform
    # because it's a low percentage, we reject H0
    # thus accepting the opposite : that we are uniform
    # with en error level of p% (or a confidence level of (1-p)%)

    # if REJECT:
    # it means that we are not uniform with an error level of p%
    # thus accepting H0 and rejecting the uniformity !
    return Kr
