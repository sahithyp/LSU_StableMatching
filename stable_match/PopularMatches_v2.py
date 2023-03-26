import random
import math
from stable_match.StableMatches import *
from stable_match.PopularMatches import generate_popular_matches

def compare_popularity(pop_match1, pop_match2, men_dict, women_dict):
    count1 = 0  # bigger count1 - more favored pop_match1 is
    count2 = 0  # bigger count2 - more favored pop_match2 is

    men_list = list(men_dict.keys())
    women_list = list(women_dict.keys())

    for i in range(len(men_list)):
        # man1 = pop_match1[i][0]
        woman1_rank = pop_match1[i][2]  # how much man1 prefers woman1
        woman2_rank = pop_match2[i][2]  # how much man1 prefers woman2

        if woman1_rank < woman2_rank:
            count1 += 1
        elif woman1_rank > woman2_rank:
            count2 += 1

        woman = women_list[i]
        woman_index1 = [elem for i, elem, j, k in pop_match1].index(woman)
        woman_index2 = [elem for i, elem, j, k in pop_match2].index(woman)

        man1_rank = pop_match1[woman_index1][3]  # how much woman1 prefers man1
        man2_rank = pop_match2[woman_index2][3]  # how much woman1 prefers man2

        if man1_rank < man2_rank:
            count1 += 1
        elif man1_rank > man2_rank:
            count2 += 1

    result = ""
    if count1 > count2:  # if true -- match1 is more popular than match2
        result = pop_match1
    elif count2 > count1:  # if true -- match2 is more popular than match1
        result = pop_match2
    else:
        return "Equal popularity"

    # result = str(result) + ", difference: " + str(abs(count1 - count2))

    return result

# obtain total popular matches parameter from generate_popular_matches function
def rank_popularity(tot_popular_matches, men_dict, women_dict):
    men_list = list(men_dict.keys())
    women_list = list(women_dict.keys())

    for i in range(len(tot_popular_matches)):
        pop_match1 = tot_popular_matches[i]
        pop_match2 = tot_popular_matches[i + 1]

        pop_match = compare_popularity(pop_match1, pop_match2, men_dict, women_dict)

        prev_pop_match = tot_popular_matches[i - 1]
        while tot_popular_matches.index(pop_match) != 0:


    return tot_popular_matches
