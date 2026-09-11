# auditor.py


total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()
    
  
    if user_input.lower() == 'quit':
        break
    
    
    if not user_input.isdigit():
        print("Error: Invalid entry. Please enter a positive whole number.")
        failed_entries += 1
        continue
    
    quantity = int(user_input)
    
    
    if quantity < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue
    
   
    total_inventory += quantity
    print(f"Added {quantity} units. Current total inventory: {total_inventory}")
    
    
    if total_inventory > 500:
        print("\n[OVERSTOCK ALERT] Total inventory exceeded 500 units! Stopping audit.")
        break


print("\n--- Audit Summary ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")