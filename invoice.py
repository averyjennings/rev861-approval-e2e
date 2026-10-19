"""Invoice arithmetic for a synthetic review fixture."""


def line_total(unit_price_cents: int, quantity: int) -> int:
    """Return the invoice line amount in integer cents.

    Each of the quantity items is charged the full unit price.
    An empty line has a total of zero cents.
    """
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("Price and quantity must be nonnegative")
    return unit_price_cents + quantity
