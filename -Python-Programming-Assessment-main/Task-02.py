from decimal import Decimal
import sys

print("1. Data Types")
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

# 2. Arithmetic operations
print("\n2. Arithmetic Operations")
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(-7 // 2)

# 3. Floating-point precision
print("\n3. Floating Point Precision")
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

# 4. Money calculation using float
print("\n4. Money Calculation")
amount = 0.1 + 0.2
print("Using float:", amount)
print("Using Decimal:", Decimal("0.1") + Decimal("0.2"))
print("Using Decimal(float):", Decimal(float(amount)))

# 5. Compare three methods
print("\n5. Comparing Money Methods")
# Method 1: Decimal
a = Decimal("0.10")
b = Decimal("0.20")
decimal_total = a + b
print("Decimal total:", decimal_total)

# Method 2: Integer paise
a_paise = 10
b_paise = 20
paise_total = a_paise + b_paise
print("Integer paise total:", paise_total, "paise")
print("Rupees:", paise_total / 100)

# Method 3: Float with rounding
a = 0.10
b = 0.20
float_total = round(a + b, 2)
print("Float total:", float_total)

# Memory usage
print("\n6. Memory Usage")
print("Decimal memory:", sys.getsizeof(decimal_total), "bytes")
print("Integer memory:", sys.getsizeof(paise_total), "bytes")
print("Float memory:", sys.getsizeof(float_total), "bytes")