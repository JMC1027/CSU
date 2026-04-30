# Part 1: Meal Cost Calculator

# Pseudocode
# Part 1
# START
# Prompt user to enter cost of food
# Store input as food_cost
# Calculate tip = food_cost * 0.18
# Calculate tax = food_cost * 0.07
# Calculate total = food_cost + tip + tax
# Display food cost
# Display tip amount
# Display tax amount
# Display total cost
# END

# Ask the user to enter the cost of the meal
food_cost = float(input("Enter the cost of the meal: "))
# Calculate the tip (18% of the food cost)
tip = food_cost * 0.18
# Calculate the tax (7% of the food cost)
tax = food_cost * 0.07
# Calculate the total cost (food + tip + tax)
total = food_cost + tip + tax
# Display a formatted summary of the meal costs
print("\n--- Meal Summary ---")
# Show the original food cost, formatted to 2 decimal places
print(f"Food Cost: ${food_cost:.2f}")
# Show the calculated tip
print(f"Tip (18%): ${tip:.2f}")
# Show the calculated tax
print(f"Tax (7%): ${tax:.2f}")
# Show the final total cost
print(f"Total Cost: ${total:.2f}")

# Part 2: Alarm Clock (24-hour format)

# START
# Part 2 
# Prompt user for current time (0–23)
# Store as current_time
# Prompt user for hours to wait
# Store as wait_time
# Calculate alarm_time = (current_time + wait_time) MOD 24
# Display alarm_time
# END
# Part 2: Alarm Clock (24-hour format)

# Ask the user to enter the current time (in hours, 0–23)
current_time = int(input("Enter current time (0-23): "))

# Ask the user how many hours to wait before the alarm goes off
wait_time = int(input("Enter hours to wait: "))

# Calculate the alarm time using modulo 24
# This keeps the result within a 24-hour clock range (0–23)
alarm_time = (current_time + wait_time) % 24

# Display the time the alarm will go off
# ":00" is added to show it's on the hour
print(f"\nThe alarm will go off at: {alarm_time}:00")
