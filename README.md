# Python_Week_3_Assignment
# Discount Calculator
## Overview

The Discount Calculator is a Python program that calculates the final price of an item after applying a discount. The function `calculate_discount` takes in two parameters: the original price and the discount percentage. It applies the discount only if the discount percentage is 20% or higher. If the discount is below 20%, the original price is returned.

## Function

### `calculate_discount(price, discount_percent)`

This function takes the original price of an item and a discount percentage, then returns the final price after applying the discount. If the discount percentage is below 20%, the function returns the original price without any changes.

#### Parameters:
- `price`: The original price of the item (float).
- `discount_percent`: The discount percentage to apply (float).

#### Returns:
- The final price after applying the discount if the discount is 20% or higher; otherwise, the original price.
