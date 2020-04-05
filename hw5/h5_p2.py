# Author: @Ross
# Functional Programing in Python

from h5_p1 import rnd_gen
from itertools import islice, filterfalse
from functools import reduce


# PART A
def gen_rndtup(m):
    """ gen_rndtup generates a sequence of tuples (a, b) where 0 <= a, b < m """
    rnd = rnd_gen(1, -1)
    while True:
        # mod both a and b by m so that a, b remain random and < m
        a = next(rnd) % m
        b = next(rnd) % m
        # yield a tuple (a, b)
        yield (a, b)


def main():

    # Part A
    gen = gen_rndtup(50)
    print(15 * '-' + ' PART A ' + 15 * '-')

    # basic iteration, print first 10 tuples with m == 50 (50 for readability)
    print(15 * '-' + ' w/o islice ' + 15 * '-')
    count = 10  # count can be infinite, only want to show the first 10
    running_count = 0
    for tup in gen:
        print('{:>3}:  {}'.format(running_count + 1, next(gen)))
        running_count += 1
        if running_count == count:
            break

    # Demonstration showing brevity of islice vs. basic iteration
    # reset gen because gen is a generator and I want two lists with the same number.
    gen = gen_rndtup(50)
    print(15 * '-' + ' islice ' + 15 * '-')
    # using islice, the second argument passed can theoretically be infinite, only showing first 10 tuples...
    first_ten = islice(gen, 0, 10)
    count = 0  # count variable used for print statement
    for tup in first_ten:
        count += 1
        print('{:>3}:  {}'.format(count, tup))

    # PART B
    print(15 * '-' + 'PART B' + 15 * '-')
    gen2 = gen_rndtup(10)

    # lambda returns True if a + b <= 6 where a,b are in tuple (a, b)
    def less_eq_six(tup): return tup[0] + tup[1] <= 6

    # lambda: y returns boolean value, since filterfalse filters out items that func() returns as false, then by saying that if less_eq_six() returns False, then the filterfalse value will generate a list that is actually items that are deamed True in the less_eq_six function. The second aruguement: the iterator, is the generator returned from Part A.
    filtered_list = filterfalse(lambda y: less_eq_six(y) == False, gen2)

    # The filterfalse list is generated first. The are an infinite amount of tuples (not unique due to short period) in the 'gen' generator. islice will stop calling the 'gen' generator to yield more tuples once it has 'collected' 8 tuples. first_eight is a generator itself.
    first_eight = islice(filtered_list, 8)

    count = 1  # used for cleaner display
    for tup in first_eight:
        print('{:>3}:  {}'.format(count, tup))
        count += 1

    # Part C
    '''Write a for loop using generator expressions and the zip function to display the first 8 tuples (a, b),
    where a is obtained using generator rnd_gen(1, -1), b is obtained using generator rnd_gen(2, -1),
    and 0 <= a <= b <= 100. The idea is to filter out tuples for which a > b -- h5 pdf description'''

    print(15 * '-' + 'PART C' + 15 * '-')

    a_it = (a % 100 for a in rnd_gen(1, -1))  # generator expression for a vals
    b_it = (b % 100 for b in rnd_gen(2, -1))  # generator expression for b vals

    # two empty lists, list will be passed to zip() later
    a_list = []
    b_list = []

    # create two lists such that all the values in a_list are less than or equal to all the values in b_list
    count = 0
    while count < 8:
        for a in a_it:
            for b in b_it:
                if a <= b:
                    a_list.append(a)
                    b_list.append(b)
                    count += 1
                    break   # start back at the first for-loop and get new values for a and b
            if count >= 8:
                break  # exit for-loop once 8 values attained, while loop will see count >= 8 and exit while loop

    zipped = zip(a_list, b_list)
    # print results
    index = 1
    for tup in zipped:
        print('{:>3}:  {}'.format(index, tup))
        index += 1

    # PART D
    '''
    Write code with the gen_rnd(1, -1) generator, lambda expressions, map(), itertools.islice,
    and the filter functions to display the first 10 random numbers between 0 and 100 that are divisible to 13.
    '''
    print('-' * 15 + 'PART D' + '-' * 15)
    values = rnd_gen(1, -1)
    modified = islice(filter(lambda x: x %
                             13 == 0, map(lambda y: y % 100, values)), 10)

    index = 1
    for value in modified:
        print('{:>3}: {:3}'.format(index, value))
        index += 1

    '''
    The above expression is quite long and is unreadable. Here is a more readable form that uses the same formula to achieve the same result:
    '''
    # first:  get values that are all less than 100
    mapped = map(lambda y: y % 100, values)
    # ...filter out those that are not divisible by 13
    filtered = filter(lambda x: x % 13 == 0, mapped)
    # ... store the first 10
    isliced = islice(filtered, 10)
    # ...print the values
    for value in isliced:
        # print(value)
        pass
    # PART E
    '''
    Write code with generator gen_rndtup(m=10) from part a), lambda expressions, map(),
    the itertools.islice, functools.reduce(), and the filter functions to display the sum of first
    10 generated tuples (a, b) that have sum a + b >= 5.
    '''
    print('-' * 15 + 'PART E' + '-' * 15)
    tuple_gen = gen_rndtup(10)  # generator
    # get first 10 tuples
    sliced = islice(filter(lambda tup: tup[0] + tup[1] >= 5, tuple_gen), 10)
    sliced_sum = map(lambda tup: tup[0] + tup[1], sliced)
    sliced_reduced = reduce(lambda a, b: a + b, sliced_sum)
    print('Sum of first 10 generated tuples that have sum a + b >= 5:  {}'.format(sliced_reduced))


if __name__ == "__main__":
    main()
