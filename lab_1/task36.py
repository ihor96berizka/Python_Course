# importing package
import matplotlib.pyplot as plt
import numpy as np

# create a main function


def main():
    # define an interval
    a = 0
    b = 2*np.pi
    # define a tab
    tab = 0.01
    # create an empty list
    ox = []
    oy_sin_x = []
    oy_cos_x = []
    oy_sin_2x = []
    # create a loop
    x = a
    while x <= b:
        ox.append(x)
        oy_sin_x.append(np.sin(x))
        oy_cos_x.append(np.cos(x))
        oy_sin_2x.append(np.sin(2 * x))
        x += tab

    # show graphs
    plt.plot(ox, oy_sin_x, label='sin(x)')
    plt.plot(ox, oy_cos_x, label='cos(x)')
    plt.plot(ox, oy_sin_2x, label='sin(2x)')
    plt.legend()
    plt.show()


main()
