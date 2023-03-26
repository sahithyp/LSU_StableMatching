from stable_match.CountIncompleteStableMatch import *


def same_mat_dim_diff_perc_complete(matrix_dim):
    # 1. run for stable matching of random combos to find average (at certain paercent)
    # a. for every 10th percent (10,20,..100%) complete, run function to find the percent stability
    # 2. repeat for multiple matrix dimensions

    same_mat_diff_percent = {}

    for percent_complete in range(50, 81, 10):
        decimal_percent = percent_complete / 100
        # print(decimal_percent)
        percent_stable = (CountStableMatches(matrix_dim, decimal_percent)) * 100

        # # Following code ensures unique values in dictionary

        # if percent_stable in same_mat_diff_percent.values():
        #     same_mat_diff_percent[percent_complete] = same_mat_diff_percent.pop(percent_complete-5)
        # else:
        #     same_mat_diff_percent[percent_complete] = percent_stable

        # # Following code simply adds each key-value pair (no checks for uniqueness)
        same_mat_diff_percent[percent_complete] = percent_stable

    # Creates dictionary with key = percent of preference lists complete and value = percent of random lists that produce stable results
    return same_mat_diff_percent


# def range_same_mat_dim_diff_perc_complete():
#     for matrix_dim in range(3, 26):
#         print("\nPercent Complete Lists vs Percent Stability %d x %d matrix" % (matrix_dim, matrix_dim))
#         print(same_mat_dim_diff_perc_complete(matrix_dim))
