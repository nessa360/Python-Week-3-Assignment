## Discount Calculator: User Friendly Discount Computation
- - Overview
- This project provides a simple, user-friendly Python script that calculates the final price of an item after applying a discount. It ensures the discount is only applied if the discount percentage is 20% or higher, and provides validation for user inputs.

## Features
- User input validation and error handling for price and discount percentage.
- Calculates the final price after applying the discount if the percentage is 20% or more.
- Returns the original price if the discount percentage is less than 20%.
- Installation
- No installation required. Just open the provided Python script in any environment supporting Python 3.

## Usage
- Open a terminal in the directory containing discount_calc.py
- Run the script with Python: python discount_calc.py
- The script will prompt you to enter the original price and the discount percentage.
- Command Line Interface:
- Enter the item price: E.g., 100.00
- Enter the discount percentage: 30
- The final price after a discount of 30% is: 70.00
- Function Details
calculate_discount(price, discount_percentage)
- Parameters:
- price: The original price of the item (a float).
- discount_percentage: The discount percentage (a float).
- Return Value:
- If discount_percentage is 20 or higher, the function returns the final price after discount (a float).
- If discount_percentage is less than 20, it returns the original price (a float).
- If invalid inputs are provided, it returns a string indicating the error.
- Error Handling
- The script uses a loop with try/except blocks to ensure valid input is provided. If the input is not a valid number, the user is prompted to enter the information again.

## Example
- Input: Item price = 100.00, Discount percentage = 30 Output: The final price after a discount of 30% is: 70.00

- Input: Item price = 100.00, Discount percentage = 19 Output: No discount applied.


## Contributing
- Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. Ensure that your code is well commented and tested.
