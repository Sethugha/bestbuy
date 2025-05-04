import products

class Store:

    def __init__(self, product_list):
        self.product_list = product_list


    def add_product(self, product):
        if product not in self.product_list:
            self.product_list.append(product)
        else:
            raise Exception("An equal product is already present!")


    def remove_product(self, product):
        if product not in self.product_list:
            raise Exception("Product not in store. Maybe a typo?")
        else:
            self.product_list.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.product_list:
                total_price += product.buy(quantity)
            else:
                continue
        return total_price

def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))


if __name__ == "__main__":
    main()
