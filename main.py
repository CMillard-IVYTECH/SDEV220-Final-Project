class Item:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name
        self.checked_out = False
        self.user = None

    def checkout(self, user):
        if not self.checked_out:
            self.checked_out = True
            self.user = user
            print(f"{self.name} checked out to {user.name}")
        else:
            print(f"{self.name} is already checked out.")

    def return_item(self):
        if self.checked_out:
            print(f"{self.name} returned from {self.user.name}")
            self.checked_out = False
            self.user = None
        else:
            print(f"{self.name} is already available.")


class User:
    def __init__(self, name):
        self.name = name


class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name):
        if item_id not in self.items:
            self.items[item_id] = Item(item_id, name)
            print(f"Item '{name}' added.")
        else:
            print("Item ID already exists.")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed_item = self.items.pop(item_id)
            print(f"Item '{removed_item.name}' removed.")
        else:
            print("Item not found.")

    def checkout_item(self, item_id, user):
        if item_id in self.items:
            self.items[item_id].checkout(user)
        else:
            print("Item not found.")

    def return_item(self, item_id):
        if item_id in self.items:
            self.items[item_id].return_item()
        else:
            print("Item not found.")

    def display_items(self):
        if not self.items:
            print("No items in inventory.")
        else:
            for item in self.items.values():
                status = "Checked out" if item.checked_out else "Available"
                print(f"ID: {item.item_id}, Name: {item.name}, Status: {status}")


# -------------------------
# TESTING (CLI FUNCTIONALITY)
# -------------------------
if __name__ == "__main__":
    manager = InventoryManager()

    manager.add_item(1, "Laptop")
    manager.add_item(2, "Calculator")

    user = User("Conner")

    manager.display_items()
    print("-----")

    manager.checkout_item(1, user)
    manager.display_items()
    print("-----")

    manager.return_item(1)
    manager.display_items()


# -------------------------
# BASIC GUI (tkinter)
# -------------------------
import tkinter as tk

manager = InventoryManager()

def add_sample_items():
    manager.add_item(1, "Laptop")
    manager.add_item(2, "Calculator")
    manager.display_items()

def checkout_item_1():
    user = User("Student")
    manager.checkout_item(1, user)

def return_item_1():
    manager.return_item(1)

def checkout_item_2():
    user = User("Student")
    manager.checkout_item(2, user)

def return_item_2():
    manager.return_item(2)

root = tk.Tk()
root.title("Campus Resource Checkout System")

tk.Label(root, text="Campus Resource Checkout System", font=("Arial", 14)).pack()

tk.Button(root, text="Add Sample Items", command=add_sample_items).pack()

tk.Button(root, text="Checkout Item 1", command=checkout_item_1).pack()
tk.Button(root, text="Return Item 1", command=return_item_1).pack()

tk.Button(root, text="Checkout Item 2", command=checkout_item_2).pack()
tk.Button(root, text="Return Item 2", command=return_item_2).pack()

root.mainloop()