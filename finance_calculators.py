# Import libraries
import math

# Create functions
# Function for calculating simple interest
def simple_interest(principal, interest_rate, time_years):
    return principal * (1 + (interest_rate/100) * time_years)

# Function for calculating compound interest
def compound_interest(principal, interest_rate, time_years):
    return principal * math.pow((1 + interest_rate/100), time_years)

# Function for calculating bond repayment
def repayment(present_value, interest_rate, time_months):
    i = (interest_rate/100)/12
    return (i * present_value)/(1 - (1 + i)**(-time_months))

# Definition for getting float
def get_float(message):

    # Helper function to get a float from the user
    returnNumber = input(message)

    while True:
        try:
            float(returnNumber)
            return float(returnNumber)

        except ValueError:
            returnNumber = input("Please enter a number: ")

def get_int(message):

    # Helper function to get a integer from the user
    returnNumber = input(message)

    while True:
        try:
            int(returnNumber)
            return int(returnNumber)

        except ValueError:
            returnNumber = input("Please enter a wholenumber / integer: ")

# Intro text. Used https://stackoverflow.com/questions/55167499/best-way-to-print-messages-on-multiple-lines
intro ="""
{}
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan
{}
""".format('-'*40, '-'*40)
print(intro)

print("Enter either 'investment' or 'bond' from the menu above to proceed:")
choice = input().strip().lower() #all valid entries will be accepted regardless of the format the user enters

# Input validation
while choice not in ["investment", "bond"] :
    print("Incorrect input. Enter either 'investment' or 'bond' from the menu above to proceed: ")
    choice = input().strip().lower()

# This block is if investment is selected 
if choice == "investment":
    principal = float(get_float("Enter the amount of money that you are depositing: "))
    interest_rate = float(get_float("Enter the interest rate as a percentage (only enter the number): "))
    time_years = int(get_int("Enter the number of years you plan on investing: "))
    interest = input("Enter '1' for simple interest or '2' for compound interest: ").strip().lower()
    # Input validation 
    while interest not in ["1", "2"] :
        print("Incorrect input. Enter '1' for simple interest or '2' for compound interest: ")
        interest = input().strip()
    

    # Calculations for investment interests
    if interest == "1":
        result = simple_interest(principal, interest_rate, time_years)
        print("Your investment will be worth " + str(result) + " after " + str(time_years) + " years with simple interest.")
    elif interest == "2":
        result = compound_interest(principal, interest_rate, time_years)
        print("Your investment will be worth " + str(result) + " after " + str(time_years) + "years with compound interest.")
        print(f"Your investment will be worth {result} after {time_years} years with compound interest.")
    else:
        print("Invalid input. Please enter either 'simple' or 'compound'.")

# This block is if bond is selected 
elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate as a percentage (only enter the number): "))
    time_months = int(input("Enter the number of months to repay the bond: "))

    # Calculations bond repayment
    result = repayment(present_value, interest_rate, time_months)
    print(f"Your bond repayment each month will be {result}.") # I tried the format function, please do let me know if there is an even more efficient way of using this.

# If user enters invalid input
else:
    print("Invalid input. Please re-run the code and enter either 'investment' or 'bond'.")

