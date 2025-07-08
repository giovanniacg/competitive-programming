from decimal import Decimal, ROUND_HALF_UP

print(Decimal(input()).to_integral_value(rounding=ROUND_HALF_UP))