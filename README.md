# Food Ordering System

A console-based food ordering application built in Python that simulates a real-world 
food ordering experience — from browsing the menu to placing an order and generating a 
final bill summary.

## Features

- Displays a formatted menu with item names and prices
- Accepts multiple item orders in a single session
- Validates user input (handles invalid items, non-numeric quantities, and negative numbers)
- Automatically updates quantity if the same item is ordered more than once
- Generates an itemized order summary with individual and total costs
- Gracefully handles users placing no order

## Tech Stack

Python (no external libraries — uses core Python only)

## How it works

1. The program displays the menu (item name + price) using a dictionary
2. The user enters item names one at a time, or types `done` to finish
3. For each valid item, the user is asked for a quantity
   - Invalid quantities (negative numbers, non-numeric input) are rejected with a clear error message
   - If an item not on the menu is entered, the user is prompted again
4. Once the user types `done`, an order summary is printed:
   - Each item with quantity and subtotal
   - Final total cost

## How to run

1. Clone the repository:
```bash
   git clone https://github.com/Kashish-Bhatt/Food-Ordering-System-Python.git
```
2. Navigate into the folder and run:
```bash
   python food_ordering_system.py
```
3. Follow the on-screen prompts to place your order

## Example menu

| Item   | Price |
|--------|-------|
| Pizza  | $12.50 |
| Burger | $7.75  |
| Pasta  | $10.00 |
| Salad  | $5.50  |
| Soda   | $2.00  |

## Future improvements

- Add a way to remove items from an existing order
- Persist orders to a file or database
- Add a simple GUI using Tkinter
