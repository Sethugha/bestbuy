from products import Product

class Store:
    """
    class for stores

    Attributes:
        product_list: list of product objects

    Methods:
        add_product(product_object)
            adds product object to store product list

        remove_product(product_object)
            removes product from store product list

        get_total_quantity()
            returns sum of all product items in stock

        get_all_products()
            returns a list of active products.
            A product in stock is active, aka available

        order(shopping_list)
            processes a shopping list composed of
            product/amount pairs. Triggers products´
            buy(quantity) method
            returns total price of all orders in list.
    """
    def __init__(self, product_list):
        """constructs a store with the products in product_list
        attributes: product_list, list of product objects
        """
        self.product_list = product_list


    def add_product(self, product):
        """adds product object to store if not already present"""
        if product not in self.product_list:
            self.product_list.append(product)
        else:
            raise Exception("An equal product is already present!")


    def remove_product(self, product):
        """removes product from store"""
        if product not in self.product_list:
            raise Exception("Product not in store. Maybe a typo?")
        self.product_list.remove(product)


    def get_total_quantity(self):
        """returns total quantity of all items in stock"""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """returns a list ob available products"""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        processes a list of product/amount pairs
        subtracts orders from stock, deactivates sold-out products
        and calculates the total price of all orders
        :parameter: Shopping list, containing product/amount pairs
        :returns: total price, float
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.product_list:
                total_price += product.buy(quantity)
            else:
                continue
        return total_price


def main():
    """Test for store class"""
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
