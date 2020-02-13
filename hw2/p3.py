
# Problem 3
# Ross Parsons
# Z23388473

import csv


def add(contact_list: list, contact_tuple: tuple) -> bool:
    """Part A: contact_list is a list that stores tuples, where each tuple is the contact of a person.
    True is returned and contact updated if person already in list, else the contact is appended to the list and 'False' is returned."""
    for contact in contact_list:
        if contact_tuple[0] == contact[0]:  # contact[0] is the full name
            contact = contact_tuple  # reassignment i.e. updating the contact
            return False
    # contact is appended to the end if not already in list
    contact_list.append(contact_tuple)
    # list is sorted. Sort is based on the first element of each tuple in a Python list of tuples.
    contact_list.sort()
    return True


def remove(contact_list: list, contact_tuple: tuple) -> bool:
    """ Part B: Removes contact from contact list if contact is in contact list and returns True, other wise False is
    returned. """
    for contact in contact_list:
        if contact_tuple[0] == contact[0]:
            contact_list.remove(contact)  # called the list method remove()
            return True
    print('Contact not found. Cannot remove.')
    return False


def search(contact_list: list, **kwargs: str) -> tuple:
    """ Part C: search() returns the contact the user is searching for. Name or Nickname is passed to the function
    in the form a kwarg where **kwargs is a dictionary e.g. ( (one=1, two=2) = {'one': 1, 'two': 2}) and the argument passed in is
    a value to the dictionary. If the value of the value passed in is in the kwarg dictionary, then the contact the user is searching
    for is in the contact list and is returned. Otherwise None is returned. """
    for contact in contact_list:
        for value in kwargs.values():
            if value in contact:
                return contact
    else:
        print('Contact not found.')
        return None


def save(contact_list: list, csv_file) -> None:
    """Part D: save() will save the contact list to file. User passes two parameters, first is a contact
    list that the user would like to store. The second parameter is a CSV file - the location the contact
    list will be stored to. This function returns nothing. """
    try:
        contact_csv_file = open(csv_file, 'w', encoding='utf-8')
    except FileNotFoundError as f:
        print('File could not be found. Please ensure filename is correct.')

    writer = csv.writer(contact_csv_file)
    for contact in contact_list:
        writer.writerow(contact)
    contact_csv_file.close()


def read(contact_csv_file):
    """Part E: The read() function takes as parameter, a CSV file which is read from, and returns the contact
    list sorted by name. """

    try:
        csv_file = open(contact_csv_file, 'r')
    except FileNotFoundError as f:
        print('File could not be found. Please ensure filename is correct.')

    reader = csv.reader(csv_file)

    contact_list = []
    for line in csv_file:
        line = tuple(line.strip().split(','))
        contact_list.append(line)
    contact_list.sort()
    return contact_list


def main():
    ''' Part F: the main function tests all of these function in parts a - e. '''
    contact_list_provided = [("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B",
                                                                         "Belcalis", "305-4399521"), ("Earl Simmons", "DMX", "305-1010101")]

    # Part A
    contact_list = []
    add_response = True
    while add_response == True:
        try:
            print('Enter a contact to add (name, nickname, phone) seperated by newline: ')
            name = input('Name: ')
            nickname = input('Nickname: ')
            phone = input('Phone number: ')
            contact = (name.lower(), nickname.lower(), phone)
            add(contact_list, contact)
            add_response = input(
                'Would you like to add another contact? (Y or N) ')
            if add_response.lower() == 'n' or add_response.lower() == 'no':
                add_response = False
            else:
                add_response = True
        except:
            continue

    print('Updated contact list: ')
    for contact in contact_list:
        print(contact)
    print(('\n'))

    # Part B

    remove_response = True
    while remove_response == True:
        try:
            remove_response = input(
                'Would you like to remove a contact? (Y or N) ')
            if remove_response.lower() == 'n' or remove_response.lower() == 'no':
                remove_response = False
                break
            else:
                remove_response = True
            print(
                'Enter a contact to remove (name, nickname, phone) seperated by newline: ')
            name = (input('Name: '))
            nickname = input('Nickname: ')
            phone = input('Phone number: ')
            contact = (name.lower(), nickname.lower(), phone)
            remove(contact_list, contact)
        except:
            continue
    print('Updated contact list: ')
    if len(contact_list) == 0:
        print('List is empty')
    for contact in contact_list:
        print(contact)
    print(('\n'))

    # Part C, search using name or nickname
    contact_list_part_c = [("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B", "Belcalis", "305-4399521"),
                           ("Earl Simmons", "DMX", "305-1010101"), ("Ross Parsons", "BOSS", '561-598-4520')]
    search_response = True
    while search_response == True:
        try:
            search_response = input(
                'Would you like to search for a contact? (Y or N) ')
        except:
            print('Please enter Y or N: ')
        if search_response.lower() == 'n' or search_response.lower() == 'no':
            search_response = False
            break
        else:
            search_response = True
            query = input(
                'Who would you like to search for? (enter name or nickname) ')
            # Pass in query as the value. Case insensitive.
            contact = search(contact_list, value=query.lower())
            print(contact)

    # Part D - save the contact list to a CSV file. (contacts.csv)
    save(contact_list, 'contacts.csv')

    # Part E testing the read function. Read from csv of contacts and print the sorted list.
    contact_csv = 'part_e_contacts.csv'
    sorted_list = read('contacts.csv')
    for contact in sorted_list:
        print(contact)


# Call main()
main()
