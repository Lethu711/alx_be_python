def display_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")

def add_item(item_list):
    item = input("Enter the item to add: ")
    if not item.strip():
        print("Item cannot be empty.")
        return
    if item.lower() in (i.lower() for i in item_list):
        print(f"{item} is already in the shopping list.")
    else:
        item_list.append(item)
        print(f"{item} has been added to the shopping list.")

def remove_item(item_list):
    item = input("Enter the item to remove: ")
    if not item.strip():
        print("Item cannot be empty.")
        return
    for existing_item in item_list:
        if existing_item.lower() == item.lower():
            item_list.remove(existing_item)
            print(f"{existing_item} has been removed from the shopping list.")
            return
    print(f"{item} is not in the shopping list.")

def view_list(item_list):
    if not item_list:
        print("The shopping list is empty.")
    else:
        print("\nShopping List:")
        for index, item in enumerate(item_list, start=1):
            print(f"{index}. {item}")

def main():
    print("Shopping List Manager")
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()

