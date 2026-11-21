import math

# Given values
fat = 4.2
snf = 8.8
quantity = 10
base_rate = 50
fat_adjustment = 2
snf_adjustment = 1

# 1. Calculate fat steps relative to 3.5%
fat_steps = round((fat - 3.5) / 0.1)
print("Fat steps:", fat_steps)

# 2. Calculate SNF steps relative to 8.5%
snf_steps = round((snf - 8.5) / 0.1)
print("SNF steps:", snf_steps)

# 3. Calculate rate per litre and payment
rate = base_rate + (fat_steps * fat_adjustment) + (snf_steps * snf_adjustment)
payment = rate * quantity

print("Rate per litre:", rate)
print("Payment amount:", payment)

# 4. Floating-point unexpected result
print("\nFloating-point result:")
print((4.2 - 3.5) / 0.1)
print(round((4.2 - 3.5) / 0.1))

# 5. Operator precedence and associativity
print("\nOperator precedence:")
print(2 ** 3 ** 2)
print(-2 ** 2)
print((-2) ** 2)

# 6. Compare round(), int(), and math.floor()
print("\nNegative value comparison:")
x = -2.7
print("round:", round(x))
print("int:", int(x))
print("floor:", math.floor(x))

# 7. Comparison chaining and Boolean operators
print("\nComparison:")
print(2.0 <= fat <= 7.0)
print(fat >= 2.0 and fat <= 7.0)
print(fat > 5.0 or snf > 8.5)
print(not (fat < 2.0))

# 8. Compare step calculation methods
print("\nStep calculation comparison:")
for value in [4.2, 3.1]:
    difference = (value - 3.5) / 0.1
    print("\nFat:", value)
    print("Using round:", round(difference))
    print("Using int:", int(difference))
    print("Using floor:", math.floor(difference))