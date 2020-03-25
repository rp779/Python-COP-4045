# Problem 2
# @author: Ross

import sys     # sys.exit()
import testif  # testif module
import turtle  # Part A


def draw_leaf_straight(length, level):
    """PART A: The draw_leaf_straight() function takes two arguments (length and level) and returns a graphic that depicts a leaf drawn in turtle graphics. """
    if level <= 0:  # base cass
        return
    else:  # recursive case
        turtle.forward(length)
        draw_leaf_straight(0.6*length, level-1)  # draws all middle branches
        turtle.left(45)
        draw_leaf_straight(0.6*length, level-1)  # draws all left branches
        turtle.right(90)
        draw_leaf_straight(0.6*length, level-1)  # draws all left branches
        turtle.left(45)
        turtle.backward(length)
        return


def strB(n, base=10):
    """ PART B: strB converts n (which is in base 10) to any base between 2 and 26. This is done by checking a string containing 26 items, for the 26 possible bases the user can convert to. n is divided by base using integer division (//) and the remainder is collected (the remainder will always be less than the base) by searching in alpha_num_str. """

    class BadBase(Exception):
        """ BadBase is a subclass of the exception class. This class is used to raise an exception if a user enters a base that is not between 2 and 26, BadBase will be raised. """
        pass

    try:
        if base < 2 or base > 26:
            raise BadBase
    except BadBase:
        print('Base must be between 2 and 26. Exiting...')
        sys.exit()
    else:
        # a string representation to allow for conversion to any base between 2 and 26.
        alpha_num_str = '0123456789ABCDEFGHIJKLMNOPQ'
        # base case - if the number is less than the base, just look for the number in alpha_num_str and return it.
        if n < base:
            return alpha_num_str[n]
        else:
            # recursive case - to convert any base 10 number to any base, the general algorithm is to find the remainder of n / base,  followed by n / new quotient. Continue doing this successively and collecting the remainders on each calculation. Then return the remainders in reverse order. In strB, the remainders are calculated by n % base and then searched for in alpha_num_str and concatenated together.
            return strB(n // base, base) + alpha_num_str[n % base]


def Cnk_m(n, k):
    """ PART C: Cnk_m returns a function that tests whether the n-choose-k values have been calculated yet and stores them in a dictionary so they can be returned instead re-calculated. """

    # a dictionary that stores n-choose-k values e.g. { (n,k): value, (n,k):value } the key is a tuple - (n,k)
    cache = dict()

    def memoization_step(n, k):
        """ inner function that runs recursively. """
        if (n, k) not in cache:  # first check these particular values of (n, k) have already been calculated.
            if k == 0 or k == n:  # base case
                return 1
            else:  # recursive step. (n,k) have not been calculated and stored in the cache, so calculate them and store them in cache
                cache[(n, k)] = memoization_step(
                    n-1, k-1) + memoization_step(n-1, k)
        # if (n, k) have been calculated, simply return their value.
        return cache[(n, k)]
    return memoization_step(n, k)


def make_pairs(seq1, seq2, merge_list, accumulator=0):
    """ PART D: make_pairs() takes in two sequences (seq1, seq2) and returns a list of tuples. Each tuple contains a value from seq1 whose index matches the value in seq2. The "accumulator" argument is set to a default value of zero. On each recursive call the accumulator is incremented by 1. merge_list is passed in as an argument because the list is mutable. """

    # Get the smaller sequence
    smaller = seq1 if len(seq1) <= len(seq2) else seq2

    if accumulator == len(smaller):  # base case
        return merge_list

    else:  # recursive case

        # append values from seq1 whose index matches the index in seq2.
        merge_list.append((seq1[accumulator], seq2[accumulator]))
        accumulator += 1

    return make_pairs(seq1, seq2, merge_list, accumulator)


def main():

    # Testing functionality of Part A: draw_leaf()
    turtle.left(90)
    turtle.speed(10)
    draw_leaf_straight(120, 6)
    turtle.done()

    # Unit tests for Part B: strB()
    testif.testif(strB(100, base=2) == '1100100',
                  'Test 1: 100 -> base 2', 'PASSED: 100 converted to base 2 = 1100100', 'FAILED')
    testif.testif(strB(123456789, base=26) == 'AA44A1',
                  'Test 2: 123456789 -> base 26', 'PASSED: 123456789 converted to base 26 = AA44A1', 'FAILED')
    testif.testif(strB(1234, base=10) == '1234',
                  'Test 3: 1234 -> base 10', 'PASSED: 1234 converted to base 10 = 1234', 'FAILED')
    testif.testif(strB(100, base=16) == '64',
                  'Test 4: 100 -> base 16', 'PASSED: 100 converted to base 16 = 64', 'FAILED')

    # Unit tests for Part C: Cnk_m()
    testif.testif(Cnk_m(10, 3) == 120, 'Test 1: n-choose-k : n=10, k=3',
                  "PASSED: 10-choose-3 is 120", 'FAILED')
    testif.testif(Cnk_m(39, 12) == 3910797436, 'Test 2: n-choose-k : n=39, k=12',
                  "PASSED: 39-choose-12 is 3910797436", 'FAILED')
    testif.testif(Cnk_m(20, 4) == 4845, 'Test 3: n-choose-k : n=20, k=4',
                  "PASSED: 20-choose-4 is 4845", 'FAILED')
    testif.testif(Cnk_m(15, 8) == 6435, 'Test 4: n-choose-k : n=15, k=8',
                  "PASSED: 15-choose-8 is 6435", 'FAILED')

    # Unit tests for Part D: make_pairs()
    testif.testif(make_pairs([1, 2, 3], [4, 5, 6], []) == [(1, 4), (2, 5), (3, 6)],
                  'Test 1: make_pairs : seq1=[1,2,3], seq2=[4,5,6]', "PASSED: make_pairs([1,2,3], [4,5,6]) = [(1,4),(2,5),(3,6)]", 'FAILED')

    testif.testif(make_pairs([2, 5, 8, 11], [4, 5, 6], []) == [(2, 4), (5, 5), (8, 6)],
                  'Test 2: make_pairs : seq1=[2,5,8,11], seq2=[4,5,6]', "PASSED: make_pairs([1,2,3], [4,5,6]) == [(1,4),(2,5),(3,6)]", 'FAILED')

    testif.testif(make_pairs([], [99, 17, 4], []) == [
    ], 'Test 3: make_pairs : seq1=[], seq2=[99,17,4]', "PASSED: make_pairs([], [99,17,4]) == []", 'FAILED')

    testif.testif(make_pairs([0, 3, 4, 9, 4, 5], [7, 8, 33], []) == [(0, 7), (3, 8), (4, 33)],
                  'Test 4: make_pairs: seq1 = [0,3,4,9,4,5] seq2 = [7,8,33]', "PASSED: make_pairs([1,2,3], [4,5,6]) == [(1,4),(2,5),(3,6)]", 'FAILED')

    testif.testif(make_pairs([10, 11, 20], [2, 4, 6, 0], []) == [(10, 2), (11, 4), (20, 6)],
                  'Test 5: make_pairs : seq1=[10,11,20], seq2=[2,4,6,0]', "PASSED: make_pairs([10,11,20], [2,4,6,0]) == [(10,2),(11,4),(20,6)", 'FAILED')


main()
