import tkinter as tk
from tkinter import messagebox


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
            return f"{self.name} checked out to {user.name}."
        return f"{self.name} is already checked out."

    def return_item(self):
        if self.checked_out:
            username = self.user.name
            self.checked_out = False
            self.user = None
            return f"{self.name} returned from {username}."
        return f"{self.name} is already available."


class User:
    def __init__(self, name):
        self.name = name


class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name):
        if item_id not in self.items:
            self.items[item_id] = Item(item_id, name)
            return f"Item '{name}' added successfully."
        return "Item ID already exists."

    def remove_item(self, item_id):
        if item_id in self.items:
            removed_item = self.items.pop(item_id)
            return f"Item '{removed_item.name}' removed successfully."
        return "Item not found."

    def checkout_item(self, item_id, user):
        if item_id in self.items:
            return self.items[item_id].checkout(user)
        return "Item not found."

    def return_item(self, item_id):
        if item_id in self.items:
            return self.items[item_id].return_item()
        return "Item not found."

    def search_item(self, keyword):
        results = []
        for item in self.items.values():
            if keyword.lower() in item.name.lower():
                results.append(item)
        return results

    def get_all_items(self):
        return list(self.items.values())


# -------------------------
# GUI APPLICATION
# -------------------------
manager = InventoryManager()


# Add sample data
manager.add_item(1, "Laptop")
manager.add_item(2, "Calculator")
manager.add_item(3, "Physics Textbook")


# GUI Functions

def refresh_display(items=None):
    listbox.delete(0, tk.END)

    if items is None:
        items = manager.get_all_items()

    if not items:
        listbox.insert(tk.END, "No items found.")
        return

    for item in sorted(items, key=lambda x: x.item_id):
        status = "Checked Out" if item.checked_out else "Available"
        user_display = f" - User: {item.user.name}" if item.user else ""

        listbox.insert(
            tk.END,
            f"ID: {item.item_id} | {item.name} | {status}{user_display}"
        )



def add_item_gui():
    try:
        item_id = int(item_id_entry.get())
        name = item_name_entry.get()

        if not name:
            messagebox.showerror("Input Error", "Please enter an item name.")
            return

        result = manager.add_item(item_id, name)
        messagebox.showinfo("Add Item", result)

        refresh_display()

        item_id_entry.delete(0, tk.END)
        item_name_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Item ID must be a number.")



def remove_item_gui():
    try:
        item_id = int(item_id_entry.get())
        result = manager.remove_item(item_id)

        messagebox.showinfo("Remove Item", result)
        refresh_display()

    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid numeric Item ID.")



def checkout_item_gui():
    try:
        item_id = int(item_id_entry.get())
        username = user_entry.get()

        if not username:
            messagebox.showerror("Input Error", "Please enter a user name.")
            return

        user = User(username)
        result = manager.checkout_item(item_id, user)

        messagebox.showinfo("Checkout Item", result)
        refresh_display()

    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid numeric Item ID.")



def return_item_gui():
    try:
        item_id = int(item_id_entry.get())

        result = manager.return_item(item_id)
        messagebox.showinfo("Return Item", result)

        refresh_display()

    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid numeric Item ID.")



def search_item_gui():
    keyword = search_entry.get()

    if not keyword:
        refresh_display()
        return

    results = manager.search_item(keyword)
    refresh_display(results)


# -------------------------
# MAIN WINDOW
# -------------------------
root = tk.Tk()
root.title("Campus Resource Checkout System")
root.geometry("700x500")


# Title
header = tk.Label(
    root,
    text="Campus Resource Checkout System",
    font=("Arial", 16, "bold")
)
header.pack(pady=10)


# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Item ID
item_id_label = tk.Label(input_frame, text="Item ID:")
item_id_label.grid(row=0, column=0, padx=5, pady=5)

item_id_entry = tk.Entry(input_frame)
item_id_entry.grid(row=0, column=1, padx=5, pady=5)


# Item Name
item_name_label = tk.Label(input_frame, text="Item Name:")
item_name_label.grid(row=1, column=0, padx=5, pady=5)

item_name_entry = tk.Entry(input_frame)
item_name_entry.grid(row=1, column=1, padx=5, pady=5)


# User Name
user_label = tk.Label(input_frame, text="User Name:")
user_label.grid(row=2, column=0, padx=5, pady=5)

user_entry = tk.Entry(input_frame)
user_entry.grid(row=2, column=1, padx=5, pady=5)


# Search
search_label = tk.Label(input_frame, text="Search:")
search_label.grid(row=3, column=0, padx=5, pady=5)

search_entry = tk.Entry(input_frame)
search_entry.grid(row=3, column=1, padx=5, pady=5)


# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


add_button = tk.Button(button_frame, text="Add Item", width=15, command=add_item_gui)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Item", width=15, command=remove_item_gui)
remove_button.grid(row=0, column=1, padx=5, pady=5)

checkout_button = tk.Button(button_frame, text="Checkout Item", width=15, command=checkout_item_gui)
checkout_button.grid(row=1, column=0, padx=5, pady=5)

return_button = tk.Button(button_frame, text="Return Item", width=15, command=return_item_gui)
return_button.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(button_frame, text="Search", width=15, command=search_item_gui)
search_button.grid(row=2, column=0, padx=5, pady=5)

show_all_button = tk.Button(button_frame, text="Show All Items", width=15, command=refresh_display)
show_all_button.grid(row=2, column=1, padx=5, pady=5)


# Item Display
listbox = tk.Listbox(root, width=90, height=15)
listbox.pack(pady=10)


# Initial Display
refresh_display()


# Run GUI
root.mainloop()
