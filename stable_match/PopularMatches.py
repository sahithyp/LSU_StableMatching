import random
import math
from stable_match.StableMatches import *

# create popular matches -- n! possible combinations for nxn set
def generate_popular_matches(men_dict, women_dict):
    tot_popular_matches = []
    n = len(men_dict)
    p = math.factorial(n)
    count = 0

    while len(tot_popular_matches) < p:
        if count > 10000:
            break

        total_men = list(men_dict.keys())
        total_women = list(women_dict.keys())

        # Creating a single popular match
        popular_match = []
        for i in range(n):
            man_elem = total_men[0]
            woman_elem = total_women[random.randint(0,len(total_women)-1)]

            woman_rank = men_dict[man_elem].index(woman_elem)
            man_rank = women_dict[woman_elem].index(man_elem)
            # [[man1, woman1, how much man1 prefers woman1, how much woman1 prefers man1],..,[..]]
            match = [man_elem, woman_elem, woman_rank, man_rank]

            total_men.remove(man_elem)
            total_women.remove(woman_elem)

            popular_match.append(match)

        # add to total popular matches if popular match is unique
        if popular_match not in tot_popular_matches:
            tot_popular_matches.append(popular_match)
            count += 1

    return tot_popular_matches

def most_popular(tot_popular_matches, men_dict, women_dict):
    match1_index = 0
    while match1_index < len(tot_popular_matches):
        if match1_index == len(tot_popular_matches) - 1:
            break

        men_list = list(men_dict.keys())
        women_list = list(women_dict.keys())

        pop_match1 = tot_popular_matches[match1_index]
        pop_match2 = tot_popular_matches[match1_index + 1]

        count1 = 0      # bigger count1 - more favored pop_match1 is
        count2 = 0      # bigger count2 - more favored pop_match2 is

        for i in range(len(men_list)):
            # man1 = pop_match1[i][0]
            woman1_rank = pop_match1[i][2]      # how much man1 prefers woman1
            woman2_rank = pop_match2[i][2]      # how much man1 prefers woman2

            if woman1_rank < woman2_rank:
                count1 += 1
            elif woman1_rank > woman2_rank:
                count2 += 1

            woman = women_list[i]
            woman_index1 = [elem for i, elem, j, k in pop_match1].index(woman)
            woman_index2 = [elem for i, elem, j, k in pop_match2].index(woman)

            man1_rank = pop_match1[woman_index1][3]        # how much woman1 prefers man1
            man2_rank = pop_match2[woman_index2][3]        # how much woman1 prefers man2

            if man1_rank < man2_rank:
                count1 += 1
            elif man1_rank > man2_rank:
                count2 += 1

        if count1 > count2: # if true -- match1 is more popular than match2
            tot_popular_matches.remove(pop_match2)
        elif count2 > count1: # if true -- match2 is more popular than match1
            del tot_popular_matches[0:match1_index + 1]
            match1_index = 0
        else: # both matches equally popular
            match1_index += 1

    return tot_popular_matches

# tot_matches = generate_popular_matches(men_dict, women_dict)
# print(len(tot_matches))
# pop_matches = most_popular(tot_matches,men_dict, women_dict)
# print(len(pop_matches))

