from stable_match.CountIncompleteStableMatch import *
from stable_match.CountCompletePopularMatch import *

# for incomplete lists
def same_perc_complete_diff_matrix_dim(percent_complete):
    # 1. run for stable matching of random combos of preference lists to find average (at certain matrix dimension)
    # a. for every 25th matrix (100x100, 125x125,...200x200), run function to find the percent stability
    # 2. repeat for multiple percentages

    same_percent_diff_mat_dim = {}

    for matrix_dim in range(10, 50, 10):
        percent_stable = (CountStableMatches(matrix_dim, percent_complete))

        same_percent_diff_mat_dim[matrix_dim] = percent_stable

    # Creates dictionary with key = matrix dimension and value = percent of random lists that produce stable results
    return same_percent_diff_mat_dim


# def range_same_perc_complete_diff_matrix_dim():
#     for percent_complete in range(5, 101, 5):
#         dec_percent = percent_complete / 100
#         print("\nMatrix Dimension vs Percent Stability %d percent complete" % (percent_complete))
#         print(same_perc_complete_diff_matrix_dim(dec_percent))