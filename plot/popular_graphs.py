from stable_match.CountCompletePopularMatch import *
import matplotlib.pyplot as plt

def plot_perc_stable_by_matrix_dimen():
    print("Matrix Dimension (key) vs Percent Stability (value) with Popular Matching")
    perc_stable = {}

    for matrix_dim in range(2, 6):
        stability = CountPopStableMatches(matrix_dim)
        print("Matrix Dimension: ", matrix_dim, ", Percent of popular matches stable: ", stability)
        perc_stable[matrix_dim] = stability

    lists = sorted(perc_stable.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples

    plt.scatter(x, y, zorder=1)
    plt.plot(x,y, zorder=2)

    plt.xlabel("Matrix Dimension")
    plt.ylabel("Percent Stable")
    plt.title("Matrix Dimension vs Percent Stable")
    # plt.legend()
    plt.show()

plot_perc_stable_by_matrix_dimen()