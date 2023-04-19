"""
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
"""

def calculate_wind_chill(air_temperature: float, wind_speed: float):
    WC_OFFSET, WC_FACTOR1, WC_FACTOR2, WC_FACTOR3, WC_EXPONENT = 13.12, 0.6215, -11.37, 0.3965, 0.16
    wci = WC_OFFSET + WC_FACTOR1 * air_temperature + WC_FACTOR2 * wind_speed ** WC_EXPONENT + WC_FACTOR3 * air_temperature * wind_speed ** WC_EXPONENT
    print(f"Wind chill index: {wci}")