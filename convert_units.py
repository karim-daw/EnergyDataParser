

def convert_kwh_to_gj(kwh: float) -> float:
    # Conversion factor from kWh to GJ
    conversion_factor = 0.0036

    # Ensure the input is a positive number
    if kwh < 0:
        raise ValueError("Input kWh must be a positive number.")

    # Perform the conversion
    gj = kwh * conversion_factor
    return gj


def convert_wh_to_kwh(wh: float) -> float:
    # convertion_factor from Wh to kWh
    conversion_factor = 0.001

    if wh < 0:
        raise ValueError("Input wH must be a positive number.")

    # perform the conversion
    kwh = wh * conversion_factor
    return kwh


def convert_therm_to_kwh(therm: float) -> float:
    # convertion_factor from therm to kWh
    conversion_factor = 29.3001

    if therm < 0:
        raise ValueError("Input therm must be a positive number.")

    # perform the conversion
    kwh = therm * conversion_factor
    return kwh
