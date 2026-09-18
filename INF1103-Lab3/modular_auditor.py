# modular_auditor.py


def get_valid_input():
    """
    Prompts the user for stock quantity input.
    
    Returns:
        int | str: An integer representing valid stock quantity,
                   or the string 'quit' to signal loop termination.
    """
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    if user_input.lower() == 'quit':
        return 'quit'
    
    try:
        val = int(user_input)
        if val < 0:
            print("Invalid input. Quantity cannot be negative.")
            return None
        return val
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'quit'.")
        return None


def process_delivery(current_total, new_value):
    """
    Calculates and returns the updated running inventory total.
    
    Args:
        current_total (int): The existing inventory sum.
        new_value (int): The incoming stock delivered.
        
    Returns:
        int: The updated inventory total.
    """
    return current_total + new_value


def calculate_tax(amount):
    """
    Calculates tax (10%) on a given delivery amount.
    
    Args:
        amount (float | int): The delivery value/quantity.
        
    Returns:
        float: The calculated tax amount (10%).
    """
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """
    Prints the final summary report.
    
    Args:
        total_units (int): Final accumulated stock total.
        failed_attempts (int): Count of invalid user input attempts.
    """
    print("\n" + "=" * 35)
    print("      INVENTORY AUDIT REPORT       ")
    print("=" * 35)
    print(f"Total Deliveries Processed : {total_units}")
    print(f"Failed/Rejected Entries    : {failed_attempts}")
    print("=" * 35)


def main():
    total_inventory = 0
    total_tax_collected = 0.0
    successful_deliveries = 0
    failed_attempts = 0

    while True:
        result = get_valid_input()

        if result == 'quit':
            break
        elif result is None:
            failed_attempts += 1
        else:
            total_inventory = process_delivery(total_inventory, result)
            tax = calculate_tax(result)
            total_tax_collected += tax
            successful_deliveries += 1
            print(f"-> Delivery recorded: +{result} units | Tax for this delivery: {tax:.2f}")

    generate_report(total_inventory, failed_attempts)


if __name__ == "__main__":
    main()
