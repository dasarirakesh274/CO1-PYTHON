from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter

PAYMENT = Decimal("10.105")
CENT = Decimal("0.01")


def float_total(n):
    return sum([10.105] * n)


def decimal_total(n):
    return PAYMENT * n


def rounded_each(n):
    payment = PAYMENT.quantize(CENT, rounding=ROUND_HALF_UP)
    return payment * n


def rounded_final(n):
    return (PAYMENT * n).quantize(CENT, rounding=ROUND_HALF_UP)


def measure(function, n):
    start = perf_counter()
    result = function(n)
    elapsed = perf_counter() - start
    return result, elapsed


print("TOTAL AND EXECUTION TIME COMPARISON")
print("Count | Float Total | Decimal Total | Float Time | Decimal Time")

for n in (300, 6000, 150000):
    f_total, f_time = measure(float_total, n)
    d_total, d_time = measure(decimal_total, n)
    print(
        f"{n} | {f_total:.2f} | {d_total:.2f} | "
        f"{f_time:.6f}s | {d_time:.6f}s"
    )

print("\nROUNDING COMPARISON FOR 300 PAYMENTS")
print("Round each payment:", rounded_each(300))
print("Round final total:", rounded_final(300))


def calculate_rate(fat, snf):
    return 30 + (fat - 3.5) * 2 + (snf - 8.5) * 1


entries = [(4.0, 9.0), (3.0, 8.0), (4.0, 9.0)] * 10000
rate_table = {pair: calculate_rate(*pair) for pair in set(entries)}


def recalculate():
    return [calculate_rate(f, s) for f, s in entries]


def lookup():
    return [rate_table[(f, s)] for f, s in entries]


_, t1 = measure(lambda: recalculate(), 1)
_, t2 = measure(lambda: lookup(), 1)

print("\nRATE TABLE COMPARISON")
print(f"Recalculation time: {t1:.6f}s")
print(f"Dictionary lookup time: {t2:.6f}s")
print("Distinct rate pairs:", len(rate_table))