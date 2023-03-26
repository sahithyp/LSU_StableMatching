import numpy as np

def gen_men_keys(n):
    # define all men available
    men_keys = ["M" + str(n) for n in range(1, n + 1)]
    return men_keys

def gen_women_keys(n):
    # define all women available
    women_keys = ["W" + str(n) for n in range(1, n + 1)]
    return women_keys


def gen_complete_perm(n, gender):
    primary_permutation = []      # fill with a complete preference matrix

    for matrix in range(1001):
        primary_perm = []       # define preference row
        for prefs in range(n):
            primary_perm.append(np.random.choice((range(1,n+1)), n, replace=False).tolist())
        primary_permutation.append(primary_perm)

    permutation = [[[gender + str(elem) for elem in prefs] for prefs in matrix] for matrix in primary_permutation]
    return permutation
