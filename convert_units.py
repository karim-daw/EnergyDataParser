

def convert_kwh_to_gj(kwh: float) -> float:
    # Conversion factor from kWh to GJ
    conversion_factor = 0.0036

    # Ensure the input is a positive number
    if kwh < 0:
        raise ValueError("Input kWh must be a positive number.")

    # Perform the conversion
    gj = kwh * conversion_factor
    return gj
