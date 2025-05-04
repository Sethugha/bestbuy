import sys
import products
import store


def start(store_obj):

    function_menu = {'1': "store_obj.get_all_products()",
                     '2': store_obj.get_total_quantity,
                     '3': place_order,
                     '4': sys.exit
                     }

    while True:
        choice = display_menu()
        if choice == '1':
            products = store_obj.get_all_products()
            for product in products:
                product.show()
        elif choice == '2':
            print(store_obj.get_total_quantity())
        elif choice == '3':
            place_order(store_obj)
        else:
            sys.exit()



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

    for item in menuitems:
        print(item)
    while True:
        users_choice = input("\nEnter choice (1 - 4): ")
        if users_choice.isnumeric() and 1 <= int(users_choice) <= 4:
            return str(users_choice)
        continue


def place_order(store_obj):
    shopping_list = []
    while True:
        print("Enter 'quit' to leave")
        users_choice = input(f"Choose a product of {str(store_obj.get_all_products())}: ")
        if users_choice.lower() == "quit":
            break
        chosen_quantity = input(f"How much {users_choice} do you order? ")
        shopping_list.append((users_choice, chosen_quantity))
    total_price = store_obj.order(shopping_list)
    return f"The total price for your order is {total_price} dollars."


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)



if __name__ == "__main__":
    main()
