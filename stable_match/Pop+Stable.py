from stable_match.PopularMatches import *
from stable_match.PopularMatches_v2 import *
from generate.GenCompleteLists import *
from stable_match.CheckStable import *
import random

def generateDictionary(gender, n):
    # genderDictKeys = []
    # unique_elem = []
    gender_dict = {}

    if gender == "M":
        genderDictKeys = gen_men_keys(n)
        unique_elem = gen_complete_perm(n, "W")
    else:
        genderDictKeys = gen_women_keys(n)
        unique_elem = gen_complete_perm(n, "M")

    lst_index = random.randint(0,(len(unique_elem)-1))

    for pos in range(n):
        gender_dict[genderDictKeys[pos]] = unique_elem[lst_index][pos]

    return gender_dict

# generate men/women dictionaries
matrix_size = int(input("Enter matrix size: "))
men_dict = generateDictionary("M", matrix_size)
women_dict = generateDictionary("W", matrix_size)

print(men_dict)
print(women_dict)

# run fair stable matching and compare to gale-shapley algorithm
original_stable_match = stable_matching_orig(men_dict, women_dict)
fair_stable_match = stable_matching_fair(men_dict, women_dict)

print("original stable match: ", original_stable_match)
print("fair stable match: ", fair_stable_match)

most_pop = compare_popularity(original_stable_match, fair_stable_match, men_dict, women_dict)
print("Most popular match: ", most_pop)


# generate list of most popular matches
pop_matches = most_popular(generate_popular_matches(men_dict, women_dict),men_dict, women_dict)
print("Popular matches: ", pop_matches)

# check which of the popular matches are stable
stable_matches = []
for matching in pop_matches:
    if check_stable_complete(matching, men_dict, women_dict) == True:
        stable_matches.append(matching)

if len(stable_matches) == 0:
    print("stable matching not in popular set")
    stable_matches = stable_matching_orig(men_dict, women_dict)


print("Stable matches: ", stable_matches)

