from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
ORIGINAL_BASE_RATE = Decimal("50.00")
ORIGINAL_FAT_STEP = Decimal("2.00")
SEASONAL_BASE_RATE = Decimal("32.00")
SEASONAL_FAT_STEP = Decimal("0.45")
SNF_STEP = Decimal("1.00")
BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")
CENT = Decimal("0.01")


def money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def validate_reading(value, name, min_val, max_val):
    val = Decimal(str(value))
    if not val.is_finite() or not (min_val <= val <= max_val):
        raise ValueError(f"Invalid {name} value.")
    return val


def calculate_rate(fat, snf, season="original"):
    fat_val = validate_reading(fat, "fat", Decimal("0"), Decimal("10"))
    snf_val = validate_reading(snf, "snf", Decimal("0"), Decimal("15"))

    if season == "seasonal":
        base = SEASONAL_BASE_RATE
        fat_step = SEASONAL_FAT_STEP
    elif season == "original":
        base = ORIGINAL_BASE_RATE
        fat_step = ORIGINAL_FAT_STEP
    else:
        raise ValueError("Season must be 'original' or 'seasonal'.")

    return (
        base
        + (fat_val - STANDARD_FAT) * fat_step
        + (snf_val - STANDARD_SNF) * SNF_STEP
    )


def calculate_payment(quantity, fat, snf, season="original"):
    qty = Decimal(str(quantity))
    if not qty.is_finite() or qty < 0:
        raise ValueError("Quantity cannot be negative.")
    rate = calculate_rate(fat, snf, season)
    return money(qty * rate)


def calculate_bonus(total_quantity):
    total_qty = Decimal(str(total_quantity))
    if not total_qty.is_finite() or total_qty < 0:
        raise ValueError("Invalid total quantity.")
    if total_qty > BONUS_LIMIT:
        return money(total_qty * BONUS_RATE)
    return Decimal("0.00")


def calculate_farmer_total(entries, season="original"):
    payments = []
    total_quantity = Decimal("0.00")
    for quantity, fat, snf in entries:
        qty = Decimal(str(quantity))
        if not qty.is_finite() or qty < 0:
            raise ValueError("Quantity cannot be negative.")
        payment = calculate_payment(qty, fat, snf, season)
        payments.append(payment)
        total_quantity += qty

    milk_total = money(sum(payments, Decimal("0.00")))
    bonus = calculate_bonus(total_quantity)
    final_total = money(milk_total + bonus)
    return payments, milk_total, bonus, final_total


def run_tests():
    entries = [
        (100, "4.00", "9.00"),
        (100, "3.50", "8.50"),
        (100, "3.00", "8.00"),
    ]

    _, original_total, bonus, final = calculate_farmer_total(entries, "original")
    assert original_total == Decimal("9000.00")
    assert bonus == Decimal("0.00")
    assert final == Decimal("9000.00")

    _, seasonal_total, bonus, final = calculate_farmer_total(entries, "seasonal")
    assert seasonal_total == Decimal("9600.00")
    assert bonus == Decimal("0.00")
    assert final == Decimal("9600.00")

    assert calculate_bonus(500) == Decimal("0.00")
    assert calculate_bonus(501) == Decimal("250.50")

    bonus_entries = [(501, "3.50", "8.50")]
    _, _, bonus, final = calculate_farmer_total(bonus_entries, "seasonal")
    assert bonus == Decimal("250.50")
    assert final == Decimal("16282.50")

    assert calculate_rate("3.55", "8.65", "seasonal") == Decimal("32.1725")

    try:
        calculate_payment(-1, "3.50", "8.50")
        assert False
    except ValueError:
        pass

    try:
        calculate_payment(1, "10.01", "8.50")
        assert False
    except ValueError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()

    entries = [
        (100, "4.00", "9.00"),
        (100, "3.50", "8.50"),
        (100, "3.00", "8.00"),
    ]

    for season in ("original", "seasonal"):
        payments, milk_total, bonus, final_total = calculate_farmer_total(
            entries, season
        )
        print(f"\n{season.upper()} RATES")
        for number, payment in enumerate(payments, start=1):
            print(f"Entry {number}: Rs. {payment:.2f}")
        print(f"Milk total: Rs. {milk_total:.2f}")
        print(f"Bonus: Rs. {bonus:.2f}")
        print(f"Final total: Rs. {final_total:.2f}")