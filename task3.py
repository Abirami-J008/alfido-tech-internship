def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            break

        try:
            temperature = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature)}°F")
        elif choice == '2':
            print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature)}°C")
        elif choice == '3':
            print(f"{temperature}°C is equal to {celsius_to_kelvin(temperature)}K")
        elif choice == '4':
            print(f"{temperature}K is equal to {kelvin_to_celsius(temperature)}°C")
        elif choice == '5':
            print(f"{temperature}°F is equal to {fahrenheit_to_kelvin(temperature)}K")
        elif choice == '6':
            print(f"{temperature}K is equal to {kelvin_to_fahrenheit(temperature)}°F")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
