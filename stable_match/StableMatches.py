def stable_matching_orig(men_dict, women_dict):
    matches=[]
    single_men=[man for man in men_dict]

    while len(single_men) > 0:
        for man in single_men:
            create_match_orig(men_dict, women_dict, single_men, matches, man)
    matches = sorted(matches,key=lambda x : x[0])

    for match in matches:
        woman_rank = men_dict[match[0]].index(match[1])
        man_rank = women_dict[match[1]].index(match[0])
        # [[man1, woman1, how much man1 prefers woman1, how much woman1 prefers man1],..,[..]]
        match.append(woman_rank)
        match.append(man_rank)
    return matches


def create_match_orig(men_dict, women_dict, single_men, matches, current_man):
    for woman in men_dict[current_man]:

        prev_proposed_man=None
        prev_proposed_pair_index = 0
        for i in range(len(matches)):
            if matches[i][1] == woman:
                prev_proposed_man = matches[i][0]
                prev_proposed_pair_index = i
                break

        if woman == "WV" or prev_proposed_man is None:
            matches.append([current_man, woman])
            single_men.remove(current_man)
            break

        else:
            prev_proposed_man_rank = 0
            current_man_rank = len(women_dict) + 1

            if prev_proposed_man in women_dict[woman]:
                prev_proposed_man_rank =women_dict[woman].index(prev_proposed_man)

            if current_man in women_dict[woman]:
                current_man_rank = women_dict[woman].index(current_man)

            if (current_man_rank < prev_proposed_man_rank):
                # If the new man is more preferred, replace original man with new man
                single_men.remove(current_man)
                single_men.append(prev_proposed_man)
                matches[prev_proposed_pair_index][0] = current_man
                break

def stable_matching_fair(men_dict, women_dict):
    matches=[]
    single_men=[man for man in men_dict]

    while len(single_men) > 0:
        for man in single_men:
            create_match_fair(men_dict, women_dict, single_men, matches, man)
    matches = sorted(matches,key=lambda x : x[0])

    for match in matches:
        woman_rank = men_dict[match[0]].index(match[1])
        man_rank = women_dict[match[1]].index(match[0])
        # [[man1, woman1, how much man1 prefers woman1, how much woman1 prefers man1],..,[..]]
        match.append(woman_rank)
        match.append(man_rank)
    return matches

def create_match_fair(men_dict, women_dict, single_men, matches, current_man):
    for woman in men_dict[current_man]:

        prev_proposed_man=None
        prev_proposed_pair_index = 0
        for i in range(len(matches)):
            if matches[i][1] == woman:
                prev_proposed_man = matches[i][0]
                prev_proposed_pair_index = i
                break

        if prev_proposed_man is None:
            matches.append([current_man, woman])
            single_men.remove(current_man)
            break

        else:
            prev_proposed_man_rank = women_dict[woman].index(prev_proposed_man)

            # if current_man in women_dict[woman]:
            current_man_rank = women_dict[woman].index(current_man)

            bound = 0.2 * len(men_dict)
            if (prev_proposed_man_rank - current_man_rank) > bound:
                # If the new man is more preferred, replace original man with new man
                single_men.remove(current_man)
                single_men.append(prev_proposed_man)
                matches[prev_proposed_pair_index][0] = current_man
                break

    # woman_rank = men_dict[man_elem].index(woman_elem)
    # man_rank = women_dict[woman_elem].index(man_elem)
    # # [[man1, woman1, how much man1 prefers woman1, how much woman1 prefers man1],..,[..]]
    # match = [man_elem, woman_elem, woman_rank, man_rank]