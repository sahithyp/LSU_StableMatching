from generate.GenCompleteLists import *
from stable_match.PopularMatches import *
from stable_match.CheckStable import *

import random


# Create preference lists with nxn dimensions when x percent complete
def CountPopStableMatches(n):
    total_popular = 0
    total_stable = 0
    stable_count_lst = []

    men_dict_primary = {}
    women_dict_secondary = {}

    menDictKeys = gen_men_keys(n)
    womenDictKeys = gen_women_keys(n)

    unique_elem_men = gen_complete_perm(n, "W")
    unique_elem_women = gen_complete_perm(n, "M")

    for pos in range(n):
        men_dict_primary[menDictKeys[pos]] = []
        women_dict_secondary[womenDictKeys[pos]] = []

    def create_dicts(gender_dict, unique_pref_list, list_pos):
        lst = unique_pref_list[list_pos]

        i = 0
        for value in gender_dict.values():
            value.clear()
            for pref in lst[i]:
                value.append(pref)
            i += 1

        return gender_dict
    num_lists = len(unique_elem_men)


    for i in range(num_lists):
        num_elem_in_men_list = random.randint(0,(num_lists-1))

        men_dict_primary = create_dicts(men_dict_primary, unique_elem_men, num_elem_in_men_list)
        women_dict_secondary = create_dicts(women_dict_secondary, unique_elem_women, num_elem_in_men_list)

        popular_matches = most_popular(generate_popular_matches(men_dict_primary,women_dict_secondary), men_dict_primary, women_dict_secondary)
        total_popular += len(popular_matches)

        count_stable = 0
        for matching in popular_matches:
            print(matching)
            print("Men Dictionary", men_dict_primary)
            print("Woman Dictionary", women_dict_secondary)
            if check_stable_complete(matching, men_dict_primary, women_dict_secondary) == True:
                count_stable += 1
                total_stable += 1

        stable_count_lst.append([count_stable,total_popular])

    perc_stable = (total_stable / total_popular) * 100

    print("Number of iterations: ", len(unique_elem_men))
    print("total popular: ", total_popular)
    print("Total Stable: ", total_stable)
    return perc_stable

print(CountPopStableMatches(9))