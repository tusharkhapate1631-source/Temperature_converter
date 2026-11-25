from temperature_converter import celsius_to_fahrenheit
from temperature_converter import fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
