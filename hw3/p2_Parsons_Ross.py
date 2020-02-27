# @author: Ross Parsons
# Z23388473
# Problem 2


class Product(object):
    """ Product class is the base class of products for sale at web store. """

    def __init__(self, name, mass, quantity, price):
        self.name = name
        self.mass = float(mass)
        self.quantity = quantity
        self._price = price  # _price is 'private' variable

    def __str__(self):
        """ __str__ returns the string representation of the calling object. """
        return '{}, {:.2f}kg, {} in stock, ${:.2f}'.format(self.name, self.mass, self.quantity, self._price)

    def price(self):
        """ price() simply returns the _price attribute of the calling object """
        return self._price

    def set_price(self, new_price):
        """ set_price() sets the _price attribute to the new_price parameters"""
        self._price = new_price


class DiscountedProduct(Product):
    """ DiscountedProducts is a derived class from Products. This class used attributes from the Products class to
    apply a discount. """

    def __init__(self, discount, obj):
        Product.__init__(self, obj.name, obj.mass, obj.quantity, obj._price)
        self.discount = discount

    def __str__(self):
        """ __str__ returns the string representation of the calling object. """
        result_str = Product.__str__(self)
        result_str += ' discounted: {:.2%}'.format(self.discount)
        return result_str

    def price(self):
        """ price() returns the _price attribute of the calling object with the discount applied. """
        return self._price - self.discount * super().price()


def main():

    print('\n')  # print a new line for readability

    # create a product object for Lavalamps, priced at $100, and with 123 of them in stock:
    p = Product(name="Lavalamp", price=30, mass=0.8, quantity=123)

    print(p)  # prints "Lavalamp, $30, 0.8 kg, 123 in stock"

    print('\n')  # print a new line for readability

    print('The price of the lavalamp: ${}'.format(p.price()))  # returns 30.0
    print('\n')  # print a new line for readability
    # create a discounted  product of p, with a 20% discount:
    disc_p = DiscountedProduct(0.2, p)

    # prints "24" (24 == 30 - 20% * 30)
    print('Discounted price: ${:.2f}'.format(disc_p.price()))
    print('\n')  # print a new line for readability
    print(disc_p)  # prints "discounted 20%: Lavalamp, $24, 0.8 kg, 123 in stock"

    # now, we change the product p:
    p.set_price(20)
    print('\n')  # print a new line for readability
    print('New Price of discounted Lavalamp after calling set_price(20): ${:.2f}'.format(
        p.price()))  # Price of discounted Lavalamp: $20.00
    print('\n')  # print a new line for readability
    # the price change also affects the discounted product object that embeds p:
    print('Price of discounted lavalamp: ${:.2f}'.format(
        disc_p.price()))  # returns 16 (16 == 20 - 20% * 20)
    print('\n')  # print a new line for readability


main()
