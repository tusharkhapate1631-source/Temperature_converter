
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def celsius_to_kelvin(temp):
    if temp < -273.15:
        raise ValueError("Temperature cannot be below absolute zero.")
    return temp + 273.15


def kelvin_to_celsius(temp):
    if temp < 0:
        raise ValueError("Kelvin temperature cannot be negative.")
    return temp - 273.15


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    try:
        choice = int(input("Enter your choice (1-4): "))
        temp = float(input("Enter temperature: "))

        if choice == 1:
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp))
        elif choice == 2:
            print("Temperature in Celsius:", fahrenheit_to_celsius(temp))
        elif choice == 3:
            print("Temperature in Kelvin:", celsius_to_kelvin(temp))
        elif choice == 4:
            print("Temperature in Celsius:", kelvin_to_celsius(temp))
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")
    except (TypeError, ValueError) as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
