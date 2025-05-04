import os

# Discount calculator
def calculate_discount(price, discount_percentage):
    # check for validity of inputs
    # check for zero or negative price
    if price <= 0:
        return 'Invalid price entered. Please enter a positive number.'  
    
    # check if discount_percentage is 100 or more  
    if discount_percentage >= 100:
        return 'Invalid discount entered. Please enter a discount percentage less than 100.'

    if discount_percentage < 20:
        return price    
    
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price

# Prompting the user for input
while True:
    try:
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        break 
    except ValueError:
        os.system('clear')
        print("That's not a valid number. Please try again.")


# Calculate the final original_price after discount
final_price = calculate_discount(original_price, discount_percentage)

if type(final_price) == str:
    print(final_price)
elif final_price == original_price:
    print("No discount applied.")
else: 
    print(f"The final price after a discount of {discount_percentage}% is: {final_price:.2f}")