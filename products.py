class Product:

    def __init__(self, name, price, quantity):
        if name and price and quantity:
            if float(price) < 0 or int(quantity) < 0:
                raise Exception("Sorry, no numbers below zero.")
            self.name = name
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = True
        else:
            raise Exception("Sorry, we do not sell No-Name products! Please apply a name.")


    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.activate = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity < 0:
            raise Exception("No quantities below zero.")
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = quantity * self.price
            if self.quantity == 0:
                self.deactivate()
            return total_price
        raise Exception(f"Not enough {self.name} available.")


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
