# Online Shopping System:
#  - Define a class Product with the following attributes and methods:
#    - Attributes: name, price
#    - Method: display_info() - prints information about the product

#  - Define two classes, ElectronicProduct and ClothingProduct, that inherit from Product.
#   - Add additional attributes and methods specific to each class.
#   - For ElectronicProduct: brand
#   - For ClothingProduct: size


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


# - Define a class ShoppingCart that contains a list of Product objects and has the following methods:
#  - add_to_cart(product) - adds a product to the shopping cart
#  - display_cart() - displays the contents of the shopping cart
#  - calculate_total() - calculates and displays the total price of items in the shopping cart

# When you launch the program, you should display options which category to choose (electronics or Clothing) and Shopping Cart with all info and the sum off all items.
# Within every category there should be at least 5 different items to choose and action to `buy` or `return` to main categories selection.
# P.S Create instances of ElectronicProduct and ClothingProduct, add them to the ShoppingCart, and display the cart.


class ShoppingCart(Product):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price)
        self.electronic_prod = ElectronicProduct(name=name, price=price)
        self.clothing_prod = ClothingProduct(name=name, price=price)


# electronic_product = ElectronicProduct()
# clothing_product = ClothingProduct()
def online_shop():
    electronic_items: dict = {
        "Phone": {"price": 1199.99, "brand": "Apple"},
        "Computer": {"price": 899.99, "brand": "MSI"},
        "Fridge": {"price": 499.99, "brand": "Snaige"},
        "Vaacum cleaner": {"price": 2099.99, "brand": "Dyson"},
        "Shaver": {"price": 29.99, "brand": "Philips"},
    }
    clothing_items: dict = {
        "Hat": {"price": 15.99, "size": "Adidas"},
        "Socks": {"price": 899.99, "size": "Philipp Plein"},
        "Pants": {"price": 499.99, "size": "Balenciaga"},
        "Shirt": {"price": 79.99, "size": "Calvin Klein"},
        "Jacket": {"price": 8.99, "size": "Humana"},
    }

    print("\n-----------------\n|--Online shop--|\n-----------------")
    category = input("--Categories--\n1. Electronics\n2. Clothing\n\nSelect category: ")
    if category.isnumeric() == True:
        if category == "1":
            counter = 1

            for x in electronic_items:
                print(f"\n{counter}. {x}")
                counter += 1
                for y in electronic_items[x]:
                    print(f"{y.capitalize()}: {electronic_items[x][y]}")
            selection: str = input("\nSelect item: ")
            # values_list = list(electronic_items.values()) reiks pasirinkt kazkuri is situ
            # values_list = list(electronic_items)

            if selection.isnumeric() == True:
                selection = int(selection) - 1
                print(values_list[selection])
                # electronic_product = ElectronicProduct(name=values_list[selection])

        elif category == "2":
            print(clothing_items)
        else:
            print("There is no such selection")
    else:
        print("Please enter number from list provided without any symbols and spaces.")


online_shop()
