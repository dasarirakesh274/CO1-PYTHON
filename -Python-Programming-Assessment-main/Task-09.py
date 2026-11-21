import math

# Constants
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
MIN_FAT = 0.0
MAX_FAT = 10.0
MIN_SNF = 0.0
MAX_SNF = 15.0

BASE_RATE = 30.0
FAT_ADJUSTMENT = 2.0
SNF_ADJUSTMENT = 1.0


# Input validation
def parse_number(value):
    try:
        number = float(value)
    except (ValueError, TypeError):
        raise ValueError("Input must be numeric.")

    if not math.isfinite(number):
        raise ValueError("Input must be a finite number.")
    return number


def validate_entry(quantity, fat, snf):
    if quantity < 0:
        raise ValueError("Milk quantity cannot be negative.")
    if not (MIN_FAT <= fat <= MAX_FAT):
        raise ValueError("Fat must be between 0% and 10%.")
    if not (MIN_SNF <= snf <= MAX_SNF):
        raise ValueError("SNF must be between 0% and 15%.")


# Calculate individual payment
def calculate_payment(quantity, fat, snf):
    quantity = parse_number(quantity)
    fat = parse_number(fat)
    snf = parse_number(snf)

    validate_entry(quantity, fat, snf)

    rate = (
        BASE_RATE
        + (fat - STANDARD_FAT) * FAT_ADJUSTMENT
        + (snf - STANDARD_SNF) * SNF_ADJUSTMENT
    )
    return round(quantity * rate, 2)


# Calculate total payment
def calculate_total(entries):
    payments = []
    for quantity, fat, snf in entries:
        payments.append(calculate_payment(quantity, fat, snf))
    return payments, round(sum(payments), 2)


# Automated tests
def expect_error(function, *args):
    try:
        function(*args)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")


def run_tests():
    assert calculate_payment(10, 4.5, 9.5) == 330.00
    assert calculate_payment(10, 3.0, 8.0) == 285.00
    assert calculate_payment(10, 3.5, 8.5) == 300.00
    assert calculate_payment(1, 0, 8.5) == 23.00
    assert calculate_payment(1, 10, 8.5) == 43.00

    expect_error(parse_number, "hello")
    expect_error(calculate_payment, -1, 3.5, 8.5)
    expect_error(calculate_payment, 1, -0.1, 8.5)
    expect_error(calculate_payment, 1, 10.1, 8.5)
    expect_error(calculate_payment, 1, 3.5, -0.1)
    expect_error(calculate_payment, 1, 3.5, 15.1)

    entries = [
        (10, 4.0, 9.0),
        (8, 3.0, 8.0),
        (12, 3.5, 8.5),
        (5, 5.0, 9.0),
        (20, 4.5, 8.0),
    ]

    payments, total = calculate_total(entries)

    assert payments == [315.00, 228.00, 360.00, 167.50, 630.00]
    assert math.isclose(total, 1700.50, abs_tol=0.001)

    print("All automated tests passed!")


# Main program
def main():
    print("MILK PAYMENT CALCULATOR")
    try:
        count = int(input("Enter number of entries: "))
        if count <= 0:
            print("Number of entries must be positive.")
            return

        entries = []
        for day in range(1, count + 1):
            print(f"\nEntry {day}")
            quantity = input("Milk quantity (litres): ")
            fat = input("Fat percentage: ")
            snf = input("SNF percentage: ")

            q = parse_number(quantity)
            f = parse_number(fat)
            s = parse_number(snf)
            validate_entry(q, f, s)

            entries.append((q, f, s))

        payments, total = calculate_total(entries)

        print("\nPAYMENT REPORT")
        for day, payment in enumerate(payments, start=1):
            print(f"Entry {day}: Rs. {payment:.2f}")

        print(f"Total payment: Rs. {total:.2f}")

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    run_tests()
    main()