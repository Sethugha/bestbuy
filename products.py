class Product:
    """
    class for products

    Attributes:
        name: str
            product name
        price: float
            product price
        quantity: int
            quantity of products in stock
        active: boolean
            True if product can be sold

    Methods:
    get_quantity()
        returns quantity of product in stock

    set_quantity(quantity)
        sets the quantity in stock, overwrites old value

    is_active()
        returns if active is True or not

    activate()
        toggles active-attribute to True

    deactivate()
        toggles active-attribute to False

    show()
        returns product name, price and quantity in stock

    buy(quantity)
        desired quantity is subtracted from stock. If stock is insufficient,
        quantity is reduced to stock value.
        If stock reaches 0, product will be deactivated.
        Returns quantity multiplied with price as float.
    """

    def __init__(self, name, price, quantity):
        """
        constructs all necessary attributes for a product object
        :param name: product name, str
        :param price: product price, float
        :param quantity: quantity in stock, int
        """
        if name and price and quantity:
            if float(price) < 0 or int(quantity) < 0:
                raise Exception("Sorry, no numbers below zero.")
            self.name = name
            self.price = float(price)
            self.quantity = int(quantity)
            if self.quantity > 0:
                self.active = True
            else:
                self.active = False
        else:
            raise Exception("Sorry, we do not sell No-Name products! Please apply a name.")


    def get_quantity(self):
        """returns quantity of product in stock"""
        return self.quantity


    def set_quantity(self, quantity):
        """sets quantity of product in stock. Overwrites old value."""
        self.quantity = quantity


    def is_active(self):
        """returns if product is available"""
        return self.active


    def activate(self):
        """sets product as available"""
        self.activate = True


    def deactivate(self):
        """sets product as not available"""
        self.active = False


    def show(self):
        """returns products main attributes"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """desired quantity is subtracted from stock. If stock is insufficient,
        quantity is reduced to stock value.
        If stock reaches 0, product will be deactivated.
        Returns quantity multiplied with price as float.
        :param quantity: Number of ordered products
        :returns: total price of sold products
        """
        if quantity < 0:
            raise Exception("No quantities below zero.")
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            quantity = self.quantity
            self.quantity = 0
        total_price = quantity * self.price
        if self.quantity == 0:
            self.deactivate()
        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
