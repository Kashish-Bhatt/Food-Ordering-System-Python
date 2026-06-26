def display_menu(menu):
    """Displays the food menu."""
    print("\n--- Our Menu ---")
    for item, price in menu.items():
        print(f"{item.capitalize():<15} : ${price:.2f}")
    print("------------------")

def main():
    """Main function for the food ordering system."""
    menu = {
        "pizza": 12.50,
        "burger": 7.75,
        "pasta": 10.00,
        "salad": 5.50,
        "soda": 2.00
    }
    
    total_cost = 0.0
    order = {}

    print("Welcome to the Python Food Ordering System!")

    while True:
        display_menu(menu)
        
        user_choice = input("\nEnter the name of the item you want to order (or 'done' to finish): ").lower()
        
        if user_choice == 'done':
            break
        
        if user_choice in menu:
            try:
                quantity = int(input(f"How many {user_choice} would you like? "))
                if quantity > 0:
                    # Add to order dictionary
                    if user_choice in order:
                        order[user_choice] += quantity
                    else:
                        order[user_choice] = quantity
                    
                    item_price = menu[user_choice]
                    total_cost += item_price * quantity
                    print(f"{quantity} {user_choice}(s) added to your order.")
                else:
                    print("Invalid quantity. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number for the quantity.")
        else:
            print("Sorry, that item is not on the menu. Please try again.")

    print("\n--- Your Order Summary ---")
    if not order:
        print("You did not place any order.")
    else:
        for item, quantity in order.items():
            price = menu[item]
            item_total = price * quantity
            print(f"{item.capitalize():<15} x {quantity} = ${item_total:.2f}")
        print("-" * 25)
        print(f"Total Cost:{'':<9} ${total_cost:.2f}")
    
    print("\nThank you for your order! Enjoy your meal.")

if __name__ == "__main__":
    main()
