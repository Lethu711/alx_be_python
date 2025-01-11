# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list, item):
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Invalid input. Please enter a valid item.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("\nThe shopping list is currently empty.")

def main():
    shopping_list = []
    actions = [
        ('1', 'Apples'),
        ('1', 'Bread'),
        ('3', 'Tomatoes'),
        ('2', 'Apples'),
        ('3', 'Milk'),
        ('4', 'Eggs')
    ]
    action_index = 0
    
    while action_index < len(actions):
        choice, item = actions[action_index]
        print(f"\nSelected option: {choice}")
        
        if choice == '1':
            add_item(shopping_list, item)
        elif choice == '2':
            remove_item(shopping_list, item)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")
        
        action_index += 1

if __name__ == "__main__":
    main()

