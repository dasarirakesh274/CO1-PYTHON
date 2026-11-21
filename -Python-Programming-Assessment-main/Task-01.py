RATE_PER_FAT = 5
SNF_BONUS = 1
DAYS = 10

farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ")

# Validation
if litres < 0 or not (2 <= fat <= 7) or snf < 0:
    print("Invalid input")
else:
    rate = (fat * RATE_PER_FAT) + (snf * SNF_BONUS)
    payment = litres * rate
    total = payment * DAYS

    print("\n--- Milk Payment Details ---")
    print("Farmer ID:", farmer_id)
    print("Shift:", shift)
    print("Rate per litre: Rs.", round(rate, 2))
    print("Payment amount: Rs.", round(payment, 2))
    print("Ten-day total: Rs.", round(total, 2))