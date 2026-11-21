"""Custom utility module for Urban Retail inventory checks."""


def check_stock(quantity):
    return "In Stock" if quantity > 0 else "Out of Stock"
