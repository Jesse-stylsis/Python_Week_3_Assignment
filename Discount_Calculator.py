# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price to get the final price
        final_price = price - discount_amount
        return final_price  # Return the final price after discount
    else:
        # If the discount is less than 20%, return the original price
        return price


# Prompt user to input the original price of the item
price = float(input("Enter the original price of the item: "))

# Prompt user to input the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function to get the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# Check if the discount was applied (final price is different from the original price)
if final_price == price:
    # If no discount was applied, print the original price
    print(f"No discount applied. The original price is {final_price}")
else:
    # If discount was applied, print the final price after discount
    print(f"The final price after applying the discount is {final_price}")
