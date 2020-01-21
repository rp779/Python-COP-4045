"""
H1 problem 1

y = ax^2 + bx + c

author: @rossparsons
"""
'''
import sys
sys.exit()


xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax]) OR ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

'''


import matplotlib.pyplot as plt
import numpy as np
import math
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
        print("two solutions: {:>3.5f} and {:>3.5f}".format(x1, x2))

        y_values = []
        x_values = []

        if x1 > x2:
            unit = abs((x1 + 2) - (x2 - 2)) / 150
            number = x2 - 2  # left bound

            while number <= x1 + 2:  # graphing from left bound to right bound
                y_values.append(a * ((number)**2) + (b * (number) + c))
                x_values.append(number)
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
        plt.plot(x_values, y_values, 'b.')
        plt.show()
