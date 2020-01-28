'''
Homework 1, Question 3: Duplicated Substrings
author: Ross Parsons
'''

import matplotlib.pyplot as plt  # plt.plot(), plt.show(), etc.
import math                      # math.sqrt()
import numpy as np


def plot_function(xs, ys):
    """ This function accepts the values in the x and y directions as arrays, and then
        plots the function """

    plt.title('Quadractic Graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(axis='both')
    plt.plot(xs, ys, 'b.')
    plt.axhline(y=0, color='r')
    plt.show()


while True:
    a = (input("Enter a: "))
    if a == '':
        break
    a = int(a)
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    discriminant = (b**2) - (4 * a * c)

    # NO SOLUTIONS
    if discriminant < 0:

        # Minimum/maximum point x-value should be the center of the x range of the graph
        x = -b/(2*a)

        print("no real solutions")

        # create x_range from a range of x values and 150 samples.
        x_range = np.linspace(x - 2, x + 2, 150)
        # hold y values which i will get from iterating over the array: x_range.
        y_range = []
        for x in x_range:
            y_range.append(a * ((x)**2) + (b * (x) + c))
        print('The min value of y is: ', min(y_range))
        # PLOT GRAPH
        plot_function(x_range, y_range)

    # ONE SOLUTION
    elif discriminant == 0:

        # 2*a  # x1 = x2 = =−b±√b2−4ac/2a
        x = (-(b) + math.sqrt(discriminant))
        # format solutions to show the first 5 decimals
        print("one soluction: {:>3.5f}".format(x))
        y_range = []
        x_range = np.linspace(x - 5, x + 5, 150)

        for x in x_range:
            y_range.append(a * ((x)**2) + (b * (x) + c))

        # PLOT GRAPH
        plot_function(x_range, y_range)

    else:
        x1 = (-b - math.sqrt(discriminant))/2*a
        x2 = (-b + math.sqrt(discriminant))/2*a

        print("two solutions: {:>3.5f} and {:>3.5f}".format(x1, x2))

        y_range = []
        if x1 > x2:
            x_range = np.linspace(x2 - 2, x1 + 2, 150)
        else:
            x_range = np.linspace(x1 - 2, x2 + 2, 150)
        for x in x_range:
            y_range.append(a * ((x)**2) + (b * (x) + c))
        # PLOT GRAPH
        plot_function(x_range, y_range)
