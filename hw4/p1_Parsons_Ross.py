# Problem 1
# @author: Ross Parsons
# Z23388473

import testif as testif


def ed_read(filename, begin=0, to=-1):
    """ PART 1: Returns a string of the content in 'filename' from 'begin' until 'to', a half-open range. If the 'to' parameter exceeds the index of the file, an IndexError exception will be raised. """
    with open(filename, 'r') as read_file:
        read_file.seek(0, 2)
        end_of_file = read_file.tell()
        read_file.seek(begin)

        ret_str = ''
        try:
            if to <= end_of_file:
                read_file.seek(begin)
            else:
                raise IndexError(to)
        except IndexError as e:
            print('{} is out of range of the file.'.format(to))
        else:

            if to > -1 and to < end_of_file:
                count = begin
                while count <= to:
                    read_file.seek(count)
                    ret_str += read_file.read(1)
                    count += 1
                return ret_str

            if to == -1:
                temp_list = []
                list_of_lines = read_file.readlines()
                for line in list_of_lines:
                    temp_list.append(line.strip('\n'))
                for stripped_line in temp_list:
                    ret_str += stripped_line + '\n'
                return ret_str


def ed_find(filename, search_str):
    """ PART 2: Returns a list of index positions where 'search_str' was found in 'filename'. An empty list is returned if search_str is not found within 'filename'. """

    with open(filename, 'r') as f:
        line_list = f.readlines()  # read each line into a list of lines
        all_string_list = []  # list of all the strings in 'filename'
        index_list = []  # indices will be stored here
        for item in line_list:
            all_string_list.extend(item.split())

        # used the enumerate method to find indexs of every string. The tell() method will not work  in a for-loop.
        for index, word in enumerate(all_string_list):
            if word.lower() == search_str.lower():
                index_list.append(index)
    return index_list


def ed_replace(filename, search_str, replace_with, occurrence=-1):
    """ PART 3: Replaces 'search_str' with 'replace_with' in the file: 'filename'. If 'occurence' is -1 then the function will replace all occurences of search_str, if occurence >= 0, then then only the 'search_str' at occurence-index will be replaced. The function returns the number of times 'search_str' was replaced. """

    # returns list of index's of search_str occurences
    location_of_search_str = ed_find(filename, search_str)
    # out_file = open(filename, 'w')
    with open(filename, 'r') as rep_file:
        line_list = []
        temp_str = ""  # temp_str will store the entire file
        count = 0      # use count to compare with occurrence
        if occurrence == -1:
            # set occurence to total number of search_str's in filename and replace them all.
            occurrence = len(ed_find(filename, search_str))

        # if search_str is part of another word then we don't want to replace a part of a word.
        search_str = search_str + " "

        for line in rep_file:  # each line is string

            # if search_str is in the line and we have not replaced all the search_str's with replace_with occurrence number of times
            if search_str in line and count < occurrence:

                # concatenate temp_str with the modified line
                temp_str += line.replace(search_str, replace_with + " ")

                count += 1
            else:
                # if search_str not in line just concatenate temp_str and line.
                temp_str += line

    # write over file name with temp_str
    with open(filename, 'w') as out_file:
        out_file.write(temp_str)

    # count contains the number of times search_str was replaced with replace_with
    return count


def ed_append(filename, string):
    """ PART 4: Appends 'string' to the end of 'filename' and returns number of characters written to file. """
    # open file in 'append' mode
    with open(filename, 'a') as f:
        # write() method returns the number of characters written by default.
        # add new line after every write for readability
        return f.write(string + '\n')


def test_ed_replace():

    # the word 'the' appears in 'file.txt' 3 times
    x = ed_replace('file.txt', '&&&', '---')
    if x == 3:
        testif_bool = True
    else:
        testif_bool = False

    testif.testif(testif_bool, 'Test: ed_replace', 'SUCCESS', 'FAIL')


def test_ed_find():
    x = ed_find('file.txt', '---')
    if x == [10, 29, 41]:
        testif_bool = True
    else:
        testif_bool = False
    testif.testif(testif_bool, 'Test: ed_find', 'SUCCESS', 'FAIL')


def main():
    print(ed_read('file.txt', 0, 52))
    print(ed_find('file.txt', 'the'))
    print(ed_replace('file.txt', 'the', '&&&'))
    print(ed_append('file1.txt', 'Ross the boss is very cool.'))

    # the test_x() functions
    test_ed_replace()
    test_ed_find()


main()
