# 1. Define named constants
BASE_RATE = 50
FAT_ADJUSTMENT = 10
SNF_ADJUSTMENT = 5
MIN_LIMIT = 0
MAX_LIMIT = 100

# Display constants
print("Base Rate:", BASE_RATE)
print("Fat Adjustment:", FAT_ADJUSTMENT)
print("SNF Adjustment:", SNF_ADJUSTMENT)
print("Minimum Limit:", MIN_LIMIT)
print("Maximum Limit:", MAX_LIMIT)

# 2. Calculate payment
fat = 8
snf = 7
payment = BASE_RATE + (fat * FAT_ADJUSTMENT) + (snf * SNF_ADJUSTMENT)
print("Payment:", payment)

# 3. Dynamic typing
value = 10
print("Integer value:", value)

value = "Hello"
print("String value:", value)

# 4. Multiple assignment
a, b = 10, 20
print("Before swapping:", a, b)

# Swap values
a, b = b, a
print("After swapping:", a, b)

# 5. Store rates in a dictionary
rates = {
    "base_rate": BASE_RATE,
    "fat_adjustment": FAT_ADJUSTMENT,
    "snf_adjustment": SNF_ADJUSTMENT,
}
print("Rates:", rates)