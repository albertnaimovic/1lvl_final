# Online Shopping System:
#  - Define a class Product with the following attributes and methods:
#    - Attributes: name, price
#    - Method: display_info() - prints information about the product

#  - Define two classes, ElectronicProduct and ClothingProduct, that inherit from Product.
#   - Add additional attributes and methods specific to each class.
#   - For ElectronicProduct: brand
#   - For ClothingProduct: size

# - Define a class ShoppingCart that contains a list of Product objects and has the following methods:
#  - add_to_cart(product) - adds a product to the shopping cart
#  - display_cart() - displays the contents of the shopping cart
#  - calculate_total() - calculates and displays the total price of items in the shopping cart

# When you launch the program, you should display options which category to choose (electronics or Clothing) and Shopping Cart with all info and the sum off all items.
# Within every category there should be at least 5 different items to choose and action to `buy` or `return` to main categories selection.
# P.S Create instances of ElectronicProduct and ClothingProduct, add them to the ShoppingCart, and display the cart.


import os, time


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def display_info(self) -> str:
        return f"Product name: {self.name}\nPrice: {self.price}"


class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, brand: str) -> None:
        super().__init__(name, price)
        self.brand = brand

    def get_product_brand(self) -> str:
        return f"Product brand: {self.brand}"


class ClothingProduct(Product):
    def __init__(self, name: str, price: float, size: str) -> None:
        super().__init__(name, price)
        self.size = size

    def get_clothing_size(self) -> str:
        return f"Clothing size: {self.size}"


class ShoppingCart:
    cart_list: list = []

    def __init__(self, item: str) -> None:
        # self.items = items
        self.item = item

    def add_item_cart(self) -> list:
        self.cart_list.append(self.item)
        return self.cart_list


def select_item(items: dict, category_type: str) -> None:
    os.system("cls")
    counter = 1
    for x in items:
        print(f"\n{counter}. {x}")
        counter += 1
        for y in items[x]:
            print(f"{y.capitalize()}: {items[x][y]}")

    while True:
        try:
            selection = int(input("\nSelect item: ")) - 1
            values_list = list(items)
            selected_item = values_list[selection]
        except Exception:
            print(
                "Please enter number from list provided without any symbols and spaces."
            )
            continue
        break
    os.system("cls")
    if category_type == "electronics":
        electronic_product = ElectronicProduct(
            name=selected_item,
            price=items[selected_item]["price"],
            brand=items[selected_item]["brand"],
        )
        print(f"\nSelected product:\n\n{electronic_product.display_info()}")
        print(electronic_product.get_product_brand())
    elif category_type == "clothing":
        clothing_product = ClothingProduct(
            name=selected_item,
            price=items[selected_item]["price"],
            size=items[selected_item]["size"],
        )
        print(f"\nSelected product:\n\n{clothing_product.display_info()}")
        print(clothing_product.get_clothing_size())

    while True:
        add_item_to_cart = input(
            "\n1. Add to cart\n2. Back to menu\n\nEnter number of selection: "
        )
        if add_item_to_cart.isnumeric() == True:
            if add_item_to_cart == "1":
                ShoppingCart(item={selected_item: items[selected_item]}).add_item_cart()
                print(f"\n{selected_item} has been added to the cart.")
                time.sleep(1.5)
                break
            elif add_item_to_cart == "2":
                break
            else:
                print("\nThere is no such selection.\n")
                time.sleep(1.5)
                os.system("cls")
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces.\n"
            )
            time.sleep(1.5)
            os.system("cls")
        print(selected_item)


def online_shop() -> None:
    electronic_items: dict = {
        "Phone": {"price": 1199.99, "brand": "Apple"},
        "Computer": {"price": 899.99, "brand": "MSI"},
        "Fridge": {"price": 499.99, "brand": "Snaige"},
        "Vaacum cleaner": {"price": 2099.99, "brand": "Dyson"},
        "Shaver": {"price": 29.99, "brand": "Philips"},
    }
    clothing_items: dict = {
        "Hat": {"price": 15.99, "size": "Unisex"},
        "Socks": {"price": 899.99, "size": "43-46"},
        "Pants": {"price": 499.99, "size": "32"},
        "Shirt": {"price": 79.99, "size": "M"},
        "Jacket": {"price": 8.99, "size": "XXL"},
    }

    while True:
        os.system("cls")
        print("\n-----------------\n|--Online shop--|\n-----------------")
        category: str = input(
            "--Categories--\n1. Electronics\n2. Clothing\n3. My cart\n4. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                select_item(electronic_items, category_type="electronics")
            elif category == "2":
                select_item(clothing_items, category_type="clothing")
            elif category == "3":
                pass
            elif category == "4":
                print("\nBye.")
                break
            else:
                print("\nThere is no such selection")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)


# if __name__ == "__main__":
#     try:
online_shop()
# except Exception as err:
#     print(f"You got an error: {err}")
