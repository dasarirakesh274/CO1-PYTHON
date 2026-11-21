# TASK 5: Read Input and Convert Types

# Read clerk's entries
try:
    name = input("Enter clerk name: ")
    quantity = int(input("Enter quantity: "))
    amount = float(input("Enter amount per litre: "))

    # Calculate total amount
    total = quantity * amount

    # Display formatted output
    print("\n--- Payment Details ---")
    print(f"Clerk Name: {name}")
    print(f"Quantity: {quantity:d}")
    print(f"Amount per litre: {amount:8.2f}")
    print(f"Total Amount: {total:8.2f}")

except ValueError:
    print("Invalid input! Enter a whole number for quantity")
    print("and a valid number for amount.")