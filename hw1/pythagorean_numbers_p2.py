# Homework 1, Question 2: Pythagorean Numbers
# author: Ross Parsons


def find_Pythagorean(n):
    """ find_Pythagorean() takes an integer n and returns the all the triples from 1 to n """
    # set all to 1 because triangle cannot have a side of length 1
    a = 1  # side a
    b = 1  # side b
    c = 1  # side c

    # list used to store the triples, in tuple form. initialized to empty
    list_of_triples = []

    while c <= n:
        while b < c:
            while a < c:
                if (a**2) + (b**2) == c**2:
                    list_of_triples.append((a, b, c))
                a += 1

            b += 1
            a = 1

        c += 1
        b = 1
    # return the list of triples. each triple is store in a tuple
    return list_of_triples


n = int(input("Enter range: "))
list_of_triples = find_Pythagorean(n)

# Print message is based on whether list is empty or not
if len(list_of_triples) == 0:
    print('No triples in range {}: {} '.format(n, list_of_triples))
else:
    print('Triples in range {}: {}'.format(n, list_of_triples))
