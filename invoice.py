"""Invoice arithmetic for a synthetic review fixture."""


def line_total(unit_price_cents: int, quantity: int) -> int:
    """Return the total in cents for a nonnegative quantity of items."""
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("Price and quantity must be nonnegative")
    return unit_price_cents * quantity
