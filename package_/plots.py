import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator


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


def plot_one_variable_with_range_one_points(A, B, f, point):
    x = np.linspace(A, B, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.scatter(point, f(point), color='green', label='point')
    plt.legend()
    plt.show()


def plot_two_variables_with_start_point(x, y, f):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False, alpha=0.5)

    ax.set_zlim(np.min(Z), np.max(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter('{x:.02f}')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.scatter(x, y, f(x, y), color='yellow', label='point')
    print(x, y, f(x, y))

    plt.legend()
    plt.show()
