# Author: Ross Parsons
# Problem 4
# Z23388473


import csv


def make_dictionary_part_a():
    """ This function will create two dictionaries for the function in part a. One dictionary will be
    for the top-casts csv file and the other for top-rated csv file."""
    top_casts = open('imdb-top-casts.csv', 'r', encoding='utf-8')
    top_rated = open('imdb-top-rated.csv', 'r', encoding='utf-8')
    casts_reader = csv.reader(top_casts)
    rated_reader = csv.reader(top_rated)
    casts_dict = {}
    rated_dict = {}

    for line in casts_reader:
        # cast_dict = {title : (director, actor)}
        casts_dict[line[0]] = (line[2], line[3])
    for line in rated_reader:
         # rated_dict = {title : year}
        rated_dict[line[1]] = line[2]

    top_rated.close()
    top_casts.close()
    return casts_dict, rated_dict
    # Function will return two dictionaries:
    # casts_dict = {title : (director, actor)}
    # rated_dict = {title : year}


def make_dictionary_part_b():
    """ This function will create two dictionaries for the function in part b. One dictionary will be
    for the top-grossing csv file and the other for top-casts csv file."""
    top_grossing = open('imdb-top-grossing.csv', 'r', encoding='utf-8')
    top_director = open('imdb-top-casts.csv', 'r', encoding='utf-8')
    grossing_reader = csv.reader(top_grossing)
    director_reader = csv.reader(top_director)
    grossing_dict = {}
    director_dict = {}

    for line in grossing_reader:
        grossing_dict[line[1]] = line[3]
    for line in director_reader:
        director_dict[line[0]] = line[2]

    top_grossing.close()
    top_director.close()
    return grossing_dict, director_dict
    # Function will return two dictionaries:
    # grossing_dict = {title : box office}
    # director_dict = {title : director}


def display_collaborations():
    """displays the ranking of tuples (director, first billed actor, # of movies
    The list is in descending ordered of the total number of movies that director and that actor worked together."""

    cast_dict, rated_dict = make_dictionary_part_a()
    result_dict = {}
    for k, v in cast_dict.items():  # k = title v = (director, actor)
        for p, q in rated_dict.items():  # p = title q = year
            # convert values to lower case incase differenct csv files use different punctuation
            if p.lower() == k.lower():
                # create the result dict, result_dict = {title: (director, actor)}
                result_dict[p] = v
    result_list = []
    for value in result_dict.values():
        result_list.append(value)
    display_list = []
    for tup in result_list:
        duo_count = result_list.count(tup)
        director, actor = tup
        display_list.append((director, actor, duo_count))
    # Change the list to set and back to list. This step removes duplicate values.
    display_list = list(set(display_list))
    # I used the 'key' parameter available in the .sort() method the key parameter takes in a function and
    # that function takes in a single argument. The returned value is a key that the sort() method will
    # used to sort the complex object by. In this case, the the complex object is a list of tuples.
    display_list.sort(key=lambda index: index[2], reverse=True)
    print(" DIRECTOR - ACTOR ")
    # print the list of tuples, but limit so only the top 5 print out
    count = 0
    for director_actor_tuple in display_list:
        print(director_actor_tuple)
        count += 1
        if count == 5:
            break


def display_top_directors():
    """This function takes parses two dictionaries, and prints out the director along with highest box-office, sorted
    by highest box-office amount"""

    # grossing_dict = {title: box_offic}
    # director_dict = {title: director}
    grossing_dict, director_dict = make_dictionary_part_b()
    result_dict = {}
    display_list = []
    for k, v in grossing_dict.items():  # k = movie, v = box-office revenue
        for p, q in director_dict.items():  # p = movie q =
            if p.lower() == k.lower():
                result_dict[q] = v

    for director, box_office in result_dict.items():
        display_list.append((director, box_office))
    print("DIRECTOR - BOX OFFICE")
    display_list.sort(key=lambda index: index[1], reverse=True)
    # For tuple in the list, print out the tuple on a new line

    # print the list of tuples, but limit so only the top 5 print out
    count = 0
    for tup in display_list:
        print(tup)
        count += 1
        if count == 5:
            break


def main():
    display_collaborations()
    display_top_directors()


main()
