'''
Homework 1, Question 4: Function Visualization
author: Ross Parsons
'''

import matplotlib.pyplot as plt
import numpy as np
import math


def plot_func(function, xmin, xmax, n):
    """ Takes user input: funtion, domain, n and plots the function """
    y_values = []
    x_values = np.linspace(xmin, xmax + 1, n)
    for x in x_values:
        y_values.append(eval(function))

    plt.title('{}'.format(function))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_values, y_values, 'b-')
    plt.plot(x_values, y_values, 'b.')

    # Call the display function so that values are displayed right before plotting takes place.
    display(x_values, y_values)
    plt.show()


def display(xs, ys):
    print('{:>4} {:>11}'.format('x', 'y'))
    print('-'*30)
    i = 0
    for x in xs:
        print('{:<+10.3f}'.format(x), end=' ')
        print('{:<+8.3f}'.format(ys[i]))
        i += 1


def main():
    # Get user input
    while True:
        function = input(
            'Enter a function to compute [hit ENTER to exit program]: ')
        if function == '':
            break
        domain = input('Enter domain (xmin, xmax) seperated by space: ')
        domain = domain.split(' ')
        domain = tuple(domain)
        xmin, xmax = float(domain[0]), float(domain[1])
        n = int(input('Enter number of samples: '))
        # call plot_func() with arguments from user
        plot_func(function, xmin, xmax, n)


# call main
main()
