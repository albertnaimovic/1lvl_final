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

    def add_item_cart(self, item) -> list:
        self.cart_list.append(item)
        return self.cart_list

    def display_cart(self) -> None:
        if self.cart_list:
            os.system("cls")
            print("\n--My cart--")
            counter = 1
            for items in self.cart_list:
                for x in items:
                    print(f"\n{counter}. {x}")
                    for y in items[x]:
                        print(f"{y.capitalize()}: {items[x][y]}")
                counter += 1
            print(f"\nTotal price: {self.calculate_total()}")
            input("\nPress enter to continue...")
        else:
            print("\nCart is empty.")
            time.sleep(1.5)

    def calculate_total(self):
        total_price = 0
        for items in self.cart_list:
            for x in items:
                total_price += items[x]["price"]
        return round(total_price, 2)


shopping_cart = ShoppingCart()
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


def select_item(items: dict, category_type: str, shopping_cart=shopping_cart) -> None:
    while True:
        os.system("cls")
        counter = 1
        print("\n--List of products--")
        for x in items:
            print(f"\n{counter}. {x}")
            counter += 1
            for y in items[x]:
                print(f"{y.capitalize()}: {items[x][y]}")

        try:
            selection = int(input("\nSelect item: ")) - 1
            values_list = list(items)
            selected_item = values_list[selection]
        except Exception:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)
            continue
        break

    while True:
        os.system("cls")
        if category_type == "electronics":
            product = ElectronicProduct(
                name=selected_item,
                price=items[selected_item]["price"],
                brand=items[selected_item]["brand"],
            )
            print(f"\nSelected product:\n\n{product.display_info()}")
            print(product.get_product_brand())
        elif category_type == "clothing":
            product = ClothingProduct(
                name=selected_item,
                price=items[selected_item]["price"],
                size=items[selected_item]["size"],
            )
            print(f"\nSelected product:\n\n{product.display_info()}")
            print(product.get_clothing_size())

        add_item_to_cart = input(
            "\n1. Add to cart\n2. Back to menu\n\nEnter number of selection: "
        )
        if add_item_to_cart.isnumeric() == True:
            if add_item_to_cart == "1":
                shopping_cart.add_item_cart(item={selected_item: items[selected_item]})

                print(f"\n{selected_item} has been added to the cart.")
                time.sleep(1.5)
                break
            elif add_item_to_cart == "2":
                break
            else:
                print("\nThere is no such selection.\n")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces.\n"
            )
            time.sleep(2)


def online_shop(
    shopping_cart=shopping_cart,
    electronic_items=electronic_items,
    clothing_items=clothing_items,
) -> None:
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
                shopping_cart.display_cart()
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


if __name__ == "__main__":
    try:
        online_shop()
    except Exception as err:
        print(f"You got an error: {err}")
