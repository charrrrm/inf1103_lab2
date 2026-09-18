# modular_auditor.py

def get_valid_input():
    while True:
        user_input = input("Enter stock quantity or 'quit': ")

        if user_input.lower() == "quit":
            return "quit"

        try:
            quantity = int(user_input)

            if quantity < 0:
                print("Invalid input. Stock quantity cannot be negative.")
            else:
                return quantity

        except ValueError:
            print("Invalid input. Please enter a whole number or 'quit'.")


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def main():
    inventory = 0
    total_deliveries = 0
    failed_attempts = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        inventory = process_delivery(inventory, result)

        tax = calculate_tax(result)

        print("Delivery accepted:", result)
        print("Tax for this delivery: $", format(tax, ".2f"))

        total_deliveries += 1

    generate_report(total_deliveries, failed_attempts)


if __name__ == "__main__":
    main()
    