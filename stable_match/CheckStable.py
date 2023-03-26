def check_stable_incomplete(matches):
    count_widow = 0

    for pair in matches:
        for person in pair:
            if person.find("V") != -1:
                count_widow += 1

        if count_widow == 1:
            return False

    return True


def check_stable_complete(matching, men_dict, women_dict):
    for pair in matching:
        woman = pair[1]
        w_prefs = women_dict.get(woman)
        preferred_men = []  # list of all men ranked above man who woman is currently matched with

        for man in w_prefs:
            if w_prefs.index(man) < w_prefs.index(pair[0]):
                preferred_men.append(man)

        if len(preferred_men) != 0:
            for man in preferred_men:
                m_prefs = men_dict.get(man)

                man_index = [elem for elem, i, j, k in matching].index(man)
                current_paired_woman = matching[man_index][1]

                if m_prefs.index(woman) < m_prefs.index(current_paired_woman):
                    return False
    return True
