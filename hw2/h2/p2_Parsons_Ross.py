'''
Problem 2
Ross Parsons
Z23388473
'''

# a Write a list comprehension that returns all tuples (a,b,c),
# with a,b,c integers, such that 1<=a,b,c<=100 and a2+b2=c2.
abc = [(a, b, c) for a in range(1, 101) for b in range(1, 101)
       for c in range(1, 101) if a**2 + b**2 == c**2]
print(abc)


# b Write a list comprehension that produces a list with tuples where the first element of the tuple
# is the length of an element in the initial list, the second element of the tuple is the element
# of the initial list capitalized, and the resulting list contains only tuples for strings with
# the length longer than three characters.
some_list = ['one', 'seven', 'three', 'two', 'ten']
ret_list = [(len(i), i.upper()) for i in some_list if len(i) > 3]
print(ret_list)
print('\n\n')


# c Write a list comprehension that produces a list with the full names Lastname, Firstname format
name_list = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
# Without list comprehension
# I created the list without list comprehension first. This helped me translate into a list comprehension
reverse_list = []
for i in name_list:
    j = i.split()
    k = ' '.join(j[::-1])
    reverse_list.append(k)


# With list comprehension
# Explanation: for each element in name_list, split the element on whitespace, creating a new list. Reverse this new list
# and join the two elements together by a space. I left the above example of how to do it without list comprehension. This
# helped me understand how to make an equivalent list comprehension.

reverse_list_comprehension = [', '.join(i.split()[::-1]) for i in name_list]
print(reverse_list_comprehension)

# Write a function called concatenate that takes as parameter a separator (a string) and an arbitrary number of additional arguments,
# all strings, and that returns the concatenation of all given strings using the given separator.
# d


def concatenate(seperator: str, *args: tuple) -> list:
    """converts the tuple to a list and uses the join method to join the elements together with a string."""
    # new_list = seperator.join(my_list)
    my_list = [i for i in args]
    new_list = sep.join(my_list)
    print(new_list)
    return new_list


# helper function to get user input for concatenate()
def gather_strings() -> tuple:
    """ Returns a tuple of strings """
    list_of_strings = []
    while True:
        string = input('Enter string: ')
        if string == '':  # if user presses ENTER instead of typing in a string, the function will
                          # end and return the tuple of strings.
            break
        list_of_strings.append(string)
    tup_of_strings = tuple(list_of_strings)
    return tup_of_strings


strings_to_seperate = gather_strings()
sep = '<-->'
# pass *strings_to_seperate with '*' so that function unpacks the tuple and applies the join method
# on all of the elements in the tuple
concatenate(sep, *strings_to_seperate)
