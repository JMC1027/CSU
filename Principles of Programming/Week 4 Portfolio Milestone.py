# Online Shopping Cart
# CREATE class ItemToPurchase
#     SET item_name = "none"
#     SET item_price = 0
#     SET item_quantity = 0

#     DEFINE method print_item_cost
#         CALCULATE total_cost = item_price * item_quantity
#         DISPLAY item_name, quantity, price, and total_cost
#     END METHOD
# END CLASS


# DISPLAY "Item 1"
# CREATE item1 object
# INPUT item1 name
# INPUT item1 price
# INPUT item1 quantity

# DISPLAY "Item 2"
# CREATE item2 object
# INPUT item2 name
# INPUT item2 price
# INPUT item2 quantity

# DISPLAY "TOTAL COST"

# CALL print_item_cost for item1
# CALL print_item_cost for item2

# CALCULATE total_cost = item1 total + item2 total

# DISPLAY total_cost


# Define a class to represent an item being purchased
class ItemToPurchase:
    # Default values for item attributes
    item_name = "none"
    item_price = 0
    item_quantity = 0

    # Method to calculate and print the total cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        # Formatted Output: Item Name Quantity @ Price = Total Cost
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")

# Get user input for first item 
print("Item 1")

# Create first item object
item1 = ItemToPurchase()

# Prompt user for item details
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))
print()  # Blank line for formatting


#  Get user input for second item 
print("Item 2")

# Create second item object
item2 = ItemToPurchase()

# Prompt user for item details
item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))


# Output total cost
print("\nTOTAL COST")

# Print cost breakdown for each item
item1.print_item_cost()
item2.print_item_cost()

# Calculate total cost of both items
total_cost = (item1.item_price * item1.item_quantity) + \
             (item2.item_price * item2.item_quantity)

# Print final total
print(f"\nTotal: ${int(total_cost)}")