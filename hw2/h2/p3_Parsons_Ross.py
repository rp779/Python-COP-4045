'''
Problem 3
Ross Parsons
Z23388473
'''
import csv


def add(contact_list: list, contact_tuple: tuple) -> bool:
    ''' contact_list is a list that stores tuples, where each tuple is the contact of a person.
    True is returned and contact updated if person already in list, else the contact is appended to the list and 'False' is returned.'''
    for contact in contact_list:
        if contact_tuple[0] == contact[0]:  # contact[0] is the full name
            contact = contact_tuple  # reassignment i.e. updating the contact
            return False
    # contact is appended to the end if not already in list
    contact_list.append(contact_tuple)
    # list is sorted. Sort is based on the first element of each tuple in a Python list of tuples.
    contact_list.sort()
    return True


def remove(contact_list, contact_tuple):
    for contact in contact_list:
        if contact_tuple[0] == contact[0]:
            contact_list.remove(contact)
            return True
    return False


def search(contact_list, *kwargs):
    pass


def save(contact_list):
    contact_csv = open('contacts.csv', 'w')
    reader = csv.writer(contact_csv)
    for contact in contact_list:
        reader.writerow(contact)
    contact_csv.close()


def main():

    c_list = [("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B", "Belcalis", "305-4399521"),
              ("Earl Simmons", "DMX", "305-1010101")]


main()
