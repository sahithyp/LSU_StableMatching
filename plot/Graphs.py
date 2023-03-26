from plot.DiffPercComplete import *
from plot.DiffMatrixDimensions import *
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def plot_diff_perc_complete():
    for matrix_dim in range(5, 20, 5):
        same_mat_diff_percent = same_mat_dim_diff_perc_complete(matrix_dim)

        print("\nPercent Complete Lists vs Percent Stability %d x %d matrix" % (matrix_dim, matrix_dim))
        print(same_mat_diff_percent)

        lists = sorted(same_mat_diff_percent.items())  # sorted by key, return a list of tuples
        x, y = zip(*lists)  # unpack a list of pairs into two tuples

        plt.scatter(x, y, label="%d x %d Matrix" % (matrix_dim, matrix_dim), zorder=1)
        plt.plot(x, y, zorder=2)

    # for xy in zip(x, y):
    #     plt.annotate('(%.2f, %.2f)' % xy, xy=xy)

    plt.xlabel("Percent Complete")
    plt.ylabel("Percent Stable")
    plt.title("Percent Complete vs Percent Stable")
    plt.legend()
    plt.show()


def plot_diff_matrix_dimensions():
    print("Matrix Dimension (key) vs Percent Stability (value)")
    for percent_complete in range(30, 81, 10):
        dec_percent = percent_complete / 100



        same_percent_diff_mat_dim = same_perc_complete_diff_matrix_dim(dec_percent)

        f = open("Stability-Matches.txt", "a")
        print("\nRunning for %d percent complete: " % percent_complete, file=f)
        print(same_perc_complete_diff_matrix_dim(dec_percent), file=f)
        print("\n", file=f)
        f.close()

        lists = sorted(same_percent_diff_mat_dim.items())  # sorted by key, return a list of tuples
        x, y = zip(*lists)  # unpack a list of pairs into two tuples

        plt.scatter(x, y, label="%d %% Complete" % percent_complete, zorder=1)
        plt.plot(x,y, zorder=2)

    plt.xlabel("Matrix Dimension")
    plt.ylabel("Percent Stable")
    plt.title("Matrix Dimension vs Percent Stable")
    plt.legend()
    plt.show()


plot_diff_perc_complete()
plot_diff_matrix_dimensions()
