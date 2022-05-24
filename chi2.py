import numpy as np
from scipy.stats import chi2

def chi2_test(values, expected, df=None, pvalues=[0.1, 0.05, 0.01, 0.001]):
    df = len(values)-1 if df == None else df
    Np = np.multiply(expected, np.sum(values))
    Kr = np.sum(np.divide(np.power(np.subtract(values, Np), 2), Np))
    # crit = chi2.ppf(q=pvalue, df=df)
    [print(f"ACCEPT at {p : <6}% | {Kr : ^6.5f} <= {chi2.ppf(q=1-p, df=df) : ^7.5f} | df = {df}") if Kr <= chi2.ppf(q=1-p, df=df) else print(f"REJECT at {p : < 6}% | {Kr : ^6.5f} <= {chi2.ppf(q=1-p, df=df) : ^7.5f} | df = {df}") for p in pvalues]
    # NOTE :
    # si Kr >= à chi2.ppf(1-p)
    # ça veut dire qu'on avait p% de chance d'être dans ce cas là
    # et ça veut dire que c'est pas uniforme
    # Si Kr <= à chi2.ppf(1-p)
    # ça veut dire qu'on est uniforme et qu'on a que p% de chance de se tromper
    return Kr
