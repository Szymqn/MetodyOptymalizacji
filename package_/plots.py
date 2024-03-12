import matplotlib.pyplot as plt
import numpy as np


def plot_one_variable_with_range_and_middle(A, B, x_sr, x_1, x_2, f):
    x = np.linspace(A, B, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.scatter(x_1, f(x_1), color='green', label='f(x_1)')
    plt.scatter(x_2, f(x_2), color='blue', label='f(x_2)')
    plt.scatter(x_sr, f(x_sr), color='red', label='f(x_sr)')
    plt.legend()
    plt.show()

    print(f"f(x_1) = {x_1}, f(x_sr) = {x_sr}, f(x_2) = {x_2}")


def plot_one_variable_with_range(A, B, x_1, x_2, f):
    x = np.linspace(A, B, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.scatter(x_1, f(x_1), color='green', label='f(x_1)')
    plt.scatter(x_2, f(x_2), color='blue', label='f(x_2)')
    plt.legend()
    plt.show()

    print(f"f(x_1) = {x_1}, f(x_2) = {x_2}")
