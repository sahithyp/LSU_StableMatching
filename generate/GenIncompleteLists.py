import numpy as np

def gen_men_keys(n):
    # define all men available
    men_keys = ["M" + str(n) for n in range(1, n + 1)]
    return men_keys

def gen_women_keys(n):
    # define all women available
    women_keys = ["W" + str(n) for n in range(1, n + 1)]
    return women_keys


def gen_random_perm(n, perc_complete):
    # Generate incomplete preference lists for certain percent incomplete
    num_complete = int(perc_complete * n)

    # if percent complete is less than 1% set complete to 1%
    if num_complete < 1:
        num_complete = 1

    primary_permutation = []      # fill with a complete preference matrix

    for matrix in range(1001):
        primary_perm = []       # define preference row
        secondary_perm = []
        for prefs in range(n):
            primary_perm.append(np.random.choice((range(1,n+1)), num_complete, replace=False).tolist())
        primary_permutation.append(primary_perm)

    return primary_permutation

# def gen_random_perm_secondary(n, perc_complete):
#     primary_matrices = gen_random_perm_primary(n,perc_complete)
#
#     for matrix in range (1001):

# print(gen_random_perm(5,0.4))


def gen_incomplete_lists(n, perc_complete, gender):
    incomplete_pref_list = gen_random_perm(n, perc_complete)

    gender_spec_list = []

    # add widows to incomplete rows and include un-preferred men/women to end of each row
    for matrix in incomplete_pref_list:
        for prefs in matrix:
            prefs.append("V")
            [prefs.append(i) for i in range(1,n+1) if i not in prefs]

        if matrix not in gender_spec_list:
            gender_spec_list.append(matrix)

    gender += "{0}"
    gender_spec_list = [[[gender.format(elem) for elem in prefs] for prefs in matrix] for matrix in gender_spec_list]

    return gender_spec_list

print("\nFinal Incomplete Lists")
print(gen_incomplete_lists(5,.40,"M"))