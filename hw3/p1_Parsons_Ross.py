# @author: Ross Parsons
# Z23388473
# Problem 1

from testif import testif


class NVector(object):
    def __init__(self, *args):  # b
        """ __init__ this is the constructor that takes a collection object OR any number of arguments as parameter"""
        elems = []
        for i in args:
            # if user passes in a list - pull items out and put them in elems[]
            if type(i) == list:
                for e in i:
                    elems.append(e)
            else:  # if user passes in individual arguments, simply put them in elems[]
                elems.append(i)
        # initialize the NVector elements
        self.elements = elems

    def __len__(self):   # c
        """ __len__ uses len(self) and return length of object that calls len()"""
        return len(self.elements)

    def __getitem__(self, index):  # d
        """ __getitem overloads assignment operator '[]' to search object for item """
        try:
            return self.elements[index]
        except IndexError as e:
            print('Index out of range.')

    def __setitem__(self, index, value):  # e
        """ __setitem__ overloads index assignment operator"""
        try:
            self.elements[index] = value
        except IndexError as e:
            print('Index out of range.')

    def __str__(self):  # f
        """ __str__ defines how the print function will handle an NVector Object.
        When using the print() funtion, python implicitly calls the __str__method """
        return '{}'.format(self.elements)

    def __eq__(self, obj):  # g
        """ __eq__ overloads the '==' operator """
        return self.elements == obj.elements

    def __ne__(self, obj):  # g
        """ __ne__ overloads the '!=' operator """
        # if type(obj)
        return self.elements != obj.elements

    def __add__(self, obj):  # h
        """ __add__ overloads the + operator. This implementation allows NVector + int and NVector + NVector. """
        sum_of_objects = []
        if type(obj) == int:
            for i in range(len(self.elements)):
                sum_of_objects.append(self.elements[i] + obj)
            return NVector(sum_of_objects)
        elif type(obj) == NVector:
            for i in range(len(self.elements)):
                sum_of_objects.append(self.elements[i] + obj.elements[i])
        else:
            print('wrong type')
            raise(TypeError)
        return NVector(sum_of_objects)

    def __radd__(self, obj):  # h
        """ __radd__ is for reflexive addtition. This allows int + NVector. Calls __add__() directly. """
        try:
            return self.__add__(obj)
        except TypeError as e:
            print('Cannot add NVector Object with type other than integer.')

    def __mul__(self, obj):  # i
        """ __mul__ overloads the * operator so that two NVector instances can be multiplied together or an 
        NVector instance multiplied by an integer. Returns a new instance of NVector. """
        product_of_objects = []
        if type(obj) == int:
            for i in range(len(self.elements)):
                product_of_objects.append(self.elements[i] * obj)
            return NVector(product_of_objects)
        elif type(obj) == NVector:
            for i in range(len(self.elements)):
                product_of_objects.append(self.elements[i] * obj.elements[i])
        else:
            print('wrong type')
            raise(TypeError)
        return NVector(product_of_objects)

    def __rmul__(self, obj):  # i
        """ __rmul__ is for reflexive multiplication. Overloading __rmul__ allows for int * NVector Calls __mul__() directly. """
        try:
            return self.__mul__(obj)
        except TypeError as e:
            print('Cannot add NVector Object with type other than integer.')

    def zeros(self, n):
        """ zeros initiates a list of n zeros (0). """
        list_of_zeros = [0] * n
        return NVector(list_of_zeros)

    def __repr__(self):
        """ __repr__ is used in the interpreter to display a string representation of the NVector Object. """
        return self.__str__()


def main():
    # initializing NVector objects for testing
    vec1 = NVector([1, 2, 3])
    vec2 = NVector([1, 2, 3])
    vec3 = NVector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    vec4 = NVector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Test the __init__ method to make sure an object of type NVector is created
    print(testif(type(vec1) == NVector, '__init__',
                 '__init__ works', '__init__ does not work'))

    # c: The length of vec1 is 3
    print(testif(len(vec1) == 3, '__len__',
                 '__len__ works', '__len__ does not work'))

    # Set the vec1 index 1 to value 999 and print vec1[1] to ensure that indexing works on NVector objects
    vec1[1] = 999
    print(vec1[1])
    # d: Test indexing (__getitem__) to see that the value of vec1[1] == 999
    print(testif(vec1[1] == 999, '__getitem__',
                 '__getitem__ works', '__getitem__ does not work'))

    # e: use index assignment to set the index of vec1 to 000 and then test that __setitem__ works
    vec1[1] = 000
    print(testif(vec1[1] == 000, '__setitem__',
                 '__setitem__ works', '__setitem__ does not work'))
    # change vec1 back to original NVector([1, 2, 3]) and continue testing
    vec1 = NVector([1, 2, 3])

    # f: testing the __str__() method. The __str__ method should return a str representation of an NVector
    print(testif(type(vec1.__str__()) == str, '__str__',
                 '__str__ works', '__str__ does not work'))

    # g: vec1 and vec2 both contain a sequence of [1, 2, 3]
    print(testif(vec1 == vec2, '__eq__', '__eq__ works', '__eq__ does not work'))

    # g: vec1 == NVector([1, 2, 3]) vec3 == NVector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), they are NOT equal
    print(testif(vec1 != vec3, '__ne__', '__ne__ works', '__ne__ does not work'))

    # h: test __add__
    # vec1 + vec2 should be equal to NVector([2, 4, 6])
    print(testif(vec1 + vec1 ==
                 NVector([2, 4, 6]), '__add__', '__add__ works', '__add__ does not work'))

    # h: test __radd__
    # Test 10 + vec1 should equal NVector([11, 12, 13])
    print(testif(10 + vec1, '__radd__', '__radd__ works', '__radd__ does not work'))

    # i: vec1 * vec1 should equal NVector([1, 4, 9])
    print(testif(vec1 * vec1 ==
                 NVector([1, 4, 9]), '__mul__', '__mul__ works', '__mul__ does not work'))
    # i: 10 * vec1 should equal NVector([10, 20, 30])
    print(testif(10 * vec1, '__rmul__', '__rmul__ works', '__rmul__ does not work'))


main()
