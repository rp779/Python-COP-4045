'''
Author: @Ross
A simple generator class that uses linear congruential generator (LCG), an algorithm that yields
a sequence of pseudo-randomized numbers.
Formula to find next pseudo-random number in the sequence: Xn+1 = (aXn + c) mod m
'''


# Values to be used:
# m = 2^32
# a = 22695477
# c = 1
# seed = user input


# PART A
class RndSeq(object):
    """ The RndSeq class generates a sequence of n pseudo-random numbers startin with a seed of x0"""

    def __init__(self, x0, n):
        self.x0 = x0
        self.n = n
        self._m = 2**32
        self._a = 22695477
        self._c = 1

    def __iter__(self):
        """ Returns an iterator"""
        self.count = 0
        return self

    def __next__(self):
        """ __next__ iterates to the next element in the iterator"""
        if self.count <= self.n:
            self.xPlusOne = (self.x0 * self._a + self._c) % self._m
            self.x0 = self.xPlusOne
            self.count += 1
            return self.xPlusOne
        else:
            raise StopIteration

    def next(self):
        return self.__next__()


def rnd_gen(x0, n):
    m = 2**32
    a = 22695477
    c = 1
    if n > 0:
        for i in range(n + 1):
            xPlusOne = (x0 * a + c) % m
            x0 = xPlusOne
            n += 1
            yield xPlusOne

    else:
        while True:
            xPlusOne = (x0 * a + c) % m
            x0 = xPlusOne
            n += 1
            yield xPlusOne


def main():
    # PART A
    print('-' * 15 + 'PART A' + '-' * 15)
    rnd = RndSeq(1, 10)
    print('Using list comprehension to make list of pseudo-random numbers: ')
    rnd_list = [i for i in rnd]
    print(rnd_list)  # prints list with same values given in Homework 5 PDF

    print()
    print('Testing next() function: ')
    rnd = RndSeq(1, 2)
    it = iter(rnd)
    print(next(it))  # --> 22695478
    print(next(it))  # --> 2156045615
    next(it)         # --> raises StopIteration

    # PART B
    print('-' * 15 + 'PART B' + '-' * 15)
    print('Using for loop to generate 10 pseudo-random numbers')
    gen = rnd_gen(1, 10)
    for i in range(11):
        print(next(gen))
    print()
    print('Using list comprehension to generate 10 pseudo-random numbers:')
    gen_list = [i for i in rnd_gen(1, 10)]
    print('Generator List : {}'.format(gen_list))
    print('Calling \'list\' constructor on rnd_gen(1, 3): {}'.format(
        list(rnd_gen(1, 3))))


if __name__ == "__main__":
    main()
