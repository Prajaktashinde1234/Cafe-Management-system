class Menu:
    def __init__(self):
        self.menu_items = {
            1: {"item": "Coffee", "price": 60},
            2: {"item": "Tea", "price": 30},
            3: {"item": "Sandwich", "price": 100},
            4: {"item": "Burger", "price": 150},
            5: {"item": "Pasta", "price": 250}
        }

    def show_menu(self):
        print("\nMenu:")
        for key, value in self.menu_items.items():
            print(f"{key}. {value['item']} - Rs{value['price']:.2f}")


class Order:
    def __init__(self):
        self.items = {}
        self.total = 0.0

    def add_item(self, item_number, menu):
        item = menu.menu_items.get(item_number)
        if item:
            self.items[item['item']] = item['price']
            self.total += item['price']
            print(f"Added {item['item']} to your order.")
        else:
            print("Invalid item number.")

    def show_order(self):
        print("\nYour Order:")
        for item, price in self.items.items():
            print(f"{item}: Rs{price:.2f}")
        print(f"\nTotal: Rs{self.total:.2f}")


class Cafe:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def start(self):
        print("Welcome to the Cafe!")
        while True:
            print("\nOptions:")
            print("1. View Menu")
            print("2. Add Item to Order")
            print("3. Remove Item from Order")
            print("4. View Order")
            print("5. Checkout")
            
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.menu.show_menu()
                elif choice == 2:
                    self.menu.show_menu()
                    item_number = int(input("\nEnter the item number to add to your order: "))
                    self.order.add_item(item_number, self.menu)
                elif choice == 3:
                    item_name = input("\nEnter the name of the item to remove from your order: ")
                    self.order.remove_item(item_name)
                elif choice == 4:
                    self.order.show_order()
                elif choice == 5:
                    self.order.show_order()
                    print("\nThank you for visiting our cafe!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    cafe_system = Cafe()
    cafe_system.start()
