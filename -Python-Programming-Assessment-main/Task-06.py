# Named constants
BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30


def rate_per_litre(fat, snf):
    """Calculate the milk rate using fat and SNF percentages."""
    fat_difference = (fat - BASE_FAT) / 0.1
    snf_difference = (snf - BASE_SNF) / 0.1

    rate = (
        BASE_RATE
        + fat_difference * FAT_ADJUSTMENT
        + snf_difference * SNF_ADJUSTMENT
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate payment for the given milk quantity and quality."""
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return round(amount, 2)


def ten_day_total(payments):
    """Calculate the total payment for a farmer over ten days."""
    total = sum(payments)
    return round(total, 2)


# Main program
litres = 10.0
fat = 3.6
snf = 8.6

rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

# Example payments received over ten days
payments = [
    amount,
    300.00,
    250.00,
    307.00,
    280.00,
    310.00,
    290.00,
    275.00,
    300.00,
    295.00,
]

total = ten_day_total(payments)

print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
print("Ten-day total: Rs.", total)