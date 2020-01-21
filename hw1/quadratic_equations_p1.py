'''
Homework 1, Question 3: Duplicated Substrings
author: Ross Parsons
'''

import matplotlib.pyplot as plt  # plt.plot(), plt.show(), etc.
import math                     # math.sqrt()

while True:
    a = (input("Enter a: "))
    if a == '':
        break
    a = int(a)
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    discriminant = (b**2) - (4 * a * c)

    if discriminant < 0:
        print("no real solutions")
    elif discriminant == 0:
        x = (-(b) + math.sqrt(discriminant))/2*a  # x1 = x2 = =−b±√b2−4ac/2a
        print("one soluction: {}".format(x))

    else:
        x1 = (-b - math.sqrt(discriminant))/2*a
        x2 = (-b + math.sqrt(discriminant))/2*a
        # format solutions to show the first 5 decimals
        print("two solutions: {:>3.5f} and {:>3.5f}".format(x1, x2))

        y_values = []  # list of y-values
        x_values = []  # list of x-values

        if x1 > x2:
            # graph 150 points, plus/minus 2 to ensure roots are shown
            unit = abs((x1 + 2) - (x2 - 2)) / 150
            number = x2 - 2  # the left bound

            while number <= x1 + 2:  # graphing from left bound to right bound
                # perform ax^2 + bx + c on x values and append to list
                y_values.append(a * ((number)**2) + (b * (number) + c))
                # append x values which are numbers incremented by - unit = abs((x1 + 2) - (x2 - 2)) / 150
                x_values.append(number)
                # increment to the next x value
                number += unit
        else:
            unit = abs((x2 + 2) - (x1 - 2)) / 150
            number = x1 - 2  # left bound

            while number <= x2 + 2:  # graphing from left bound to right bound
                y_values.append(a * ((number)**2) + (b * (number) + c))
                x_values.append(number)
                number += unit

    #  PLOT THE GRAPH
        plt.title('Quadractic Graph')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(y=0, color='k')

        for point in y_values:
            if point == 0:
                plt.plot(x_values, y_values, 'or')
            else:
                plt.plot(x_values, y_values, 'b.')

        plt.show()
