'''
Homework 1, Question 3: Duplicated Substrings
author: Ross Parsons
'''


def find_dup_str(s, n):
    """
    find_dup takes in a string s and an integer n and returns the substring,
    a slice of s, with character count n. Function ends once one duplicate is found
    if a s has more than one duplicate of size n, the function will not see those duplicates.
    """
    i = 0
    j = i+n
    while i <= (len(s) - 2*n):
        while j <= (len(s) - n):
            # if duplicates :
            if s[i:i+n] == s[j:j+n]:

                # store substsring
                substring = s[i:i+n]

                # if a duplicate substring is found return it and complete function.
                return substring

            j += 1
        i += 1
        j = i+n


def find_max_dup(s):
    i = 1
    dup_list = []
    while i <= ((len(s) / 2) - 1):
        n = i
        dup = find_dup_str(s, n)
        if dup != None:
            dup_list.append(dup)
        i += 1
    max_sub = max(dup_list)
    return max_sub


def main():
    s = input("Enter string: ")
    n = int(input("Enter desired length of substring: "))
    result = find_dup_str(s, n)
    print("\tDuplicated substring of length {} in {} is: {}".format(n, s, result))

    max_sub = find_max_dup(s)
    print('\tThe max substring is: {}\n'.format(max_sub))


main()
