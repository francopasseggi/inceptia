_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]

def validate_discount_code(discount_code):

    discount_code = set(discount_code)

    for code in _AVAILABLE_DISCOUNT_CODES:
        diff = set(code) ^ discount_code  # ^ is the symmetric difference operator

        if len(diff) <= 2:
            return True
            
    return False