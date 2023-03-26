from generate.GenIncompleteLists import *
from stable_match.StableMatches import *
from stable_match.CheckStable import *
from generate.GenIncompleteLists import *

import random


# Create preference lists with nxn dimensions when x percent complete
def CountStableMatches(n, perc_complete):
    stableCount = 0
    men_dict_primary = {}
    women_dict_secondary = {}

    menDictKeys = gen_men_keys(n)
    womenDictKeys = gen_women_keys(n)

    unique_elem_men = gen_incomplete_lists(n, perc_complete, "W")
    unique_elem_women = gen_incomplete_lists(n, perc_complete, "M")

    for pos in range(n):
        men_dict_primary[menDictKeys[pos]] = []
        women_dict_secondary[womenDictKeys[pos]] = []

    def create_dicts(gender_dict, gender, unique_pref_list, list_pos):
        lst = unique_pref_list[list_pos]

        i = 0
        for value in gender_dict.values():
            value.clear()
            for pref in lst[i]:
                value.append(pref)
            i += 1

        if gender == "M":
            key_gen = "WV"
        else:
            key_gen = "MV"

        v_list = list(range(1, n + 1))
        v_list.append("V")
        gender_insert = gender + "{0}"
        v_list = [(gender_insert).format(elem) for elem in v_list]

        gender_dict[key_gen] = [str(i) for i in v_list]

        return gender_dict

    if len(unique_elem_women) < len(unique_elem_men):
        num_lists = len(unique_elem_women)
    else:
        num_lists = len(unique_elem_men)


    for i in range(num_lists):
        num_elem_in_men_list = random.randint(0,(num_lists-1))
        men_dict_primary = create_dicts(men_dict_primary, "W", unique_elem_men, num_elem_in_men_list)

        entire_men_list = gen_men_keys(n)

        for woman in women_dict_secondary.keys():
            preferred_men_list = []
            for man in men_dict_primary:
                if man != "MV":
                    if woman in men_dict_primary[man] and men_dict_primary[man].index(woman) < men_dict_primary[man].index("WV"):
                        preferred_men_list.append(man)

            if len(preferred_men_list) != 0:
                random.shuffle(preferred_men_list)
                preferred_men_list.append("MV")

            else:
                preferred_men_list.append("MV")

            for man in entire_men_list:
                if preferred_men_list.count(man) <= 0:
                    preferred_men_list.append(man)

            women_dict_secondary[woman] = preferred_men_list

        entire_men_list.append("MV")
        women_dict_secondary["WV"] = entire_men_list


        matches = stable_matching_orig(men_dict_primary, women_dict_secondary)

        if check_stable_incomplete(matches):
            stability = "Found Stable Match: "
            stableCount += 1

        else:
            stability = "No Stable Match: "

        f = open("Stability-Matches.txt", "a")
        print("\n***********************************---NEW RUN---***********************************", file=f)
        print("Men Dictionary: ", men_dict_primary, file=f)
        print("Women Dictionary: ", women_dict_secondary, file=f)

        for match in matches:
            match.append(men_dict_primary[match[0]].index(match[1]))
            match.append(women_dict_secondary[match[1]].index(match[0]))
            match.append(match[2] + match[3])

        print(stability, matches, file=f)
        f.close()


        del men_dict_primary["MV"]
        del women_dict_secondary["WV"]

    percent_stable = (stableCount / num_lists) * 100
    return percent_stable
