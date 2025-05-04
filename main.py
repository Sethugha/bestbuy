from products import Product
from store import Store


def start(store_obj):
    """
    Displays store menu in a loop, main user interface for
    store object
    :param store_obj: store object of class store.
    """
    while True:
        choice = display_menu()
        if choice == '1':
            display_products(store_obj)
        elif choice == '2':
            print(f"Total of {store_obj.get_total_quantity()} items in store")
        elif choice == '3':
            place_order(store_obj)
        else:
            break


def display_products(store_obj):
    """
    Displays products available in store. Available are products
    if they are in stock.
    :param store_obj: store selling the products
    :return: list of active aka available products
    """
    product_list = store_obj.get_all_products()
    print("------")
    for product in product_list:
        print(f"{product_list.index(product) + 1}. {product.show()}")
    print("------")


def display_menu():
    """
    Menu display, main console element. Any non-numeric input
    and numbers outside the given range are ignored.
    :returns: number of users´ choice, int
    """
    menuitems = [
                "1. List all products in store",
                "2. Show total amount in store",
                "3. Make an order",
                "4. Quit"
                ]
    print("\n   Store Menu\n   ----------")
    for item in menuitems:
        print(item)
    while True:
        users_choice = input("\nEnter choice (1 - 4): ")
        if users_choice.isnumeric() and 1 <= int(users_choice) <= 4:
            return str(users_choice)
        continue


def place_order(store_obj):
    """
    Creates a shopping list containing product/amount pairs
    which will be processed by the product objects themselves.
    :param store_obj: store object selling the products
    :return: total price of placed order.
    """
    shopping_list = []
    while True:
        print("When you want to finish order, enter empty text.")
        display_products(store_obj)
        users_choice = input("Which product # do you want? ")
        if users_choice == "":
            break
        product_list = store_obj.get_all_products()
        chosen_product = product_list[int(users_choice) - 1]
        chosen_quantity = input("What amount do you want? ")
        if not chosen_quantity.isdigit():
            break
        shopping_list.append((chosen_product, int(chosen_quantity)))
        print("Product added to list!\n")
    total_price = store_obj.order(shopping_list)
    print(f"The total price for your order is {total_price} dollars.")


def main():
    """
    Initialization of best_buy store object
    and start of store user interface
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)



if __name__ == "__main__":
    main()
