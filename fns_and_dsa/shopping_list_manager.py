def display_menu():
    """Displays the menu options."""
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    """Adds an item to the shopping list."""
    item = get_input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
    """Removes an item from the shopping list."""
    item = get_input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    """Displays the current shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("\nThe shopping list is currently empty.")

def shopping_list_manager():
    """Main function to manage the shopping list."""
    shopping_list = []

    while True:
        display_menu()
        choice = get_input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-4).")

def get_input(prompt):
    """Helper function to handle input for environments without interactive input."""
    try:
        return input(prompt)
    except OSError:
        print("Input function is not supported in this environment.")
        return "4"  

if __name__ == "__main__":
    shopping_list_manager()

