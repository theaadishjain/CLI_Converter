import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    parser = argparse.ArgumentParser(
        description="🌡️ CLI Temperature Converter (Celsius ↔ Fahrenheit)"
    )
    parser.add_argument(
        "temperature", type=float, help="Temperature value to convert"
    )
    parser.add_argument(
        "-c", "--celsius", action="store_true", help="Convert Fahrenheit to Celsius"
    )
    parser.add_argument(
        "-f", "--fahrenheit", action="store_true", help="Convert Celsius to Fahrenheit"
    )

    args = parser.parse_args()

    if args.celsius:
        result = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature}°F = {result:.2f}°C")
    elif args.fahrenheit:
        result = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature}°C = {result:.2f}°F")
    else:
        print("❌ Please specify either --celsius or --fahrenheit. Use -h for help.")

if __name__ == "__main__":
    main()
