# ------------------------------------------------------------------------------
# Name:         finance_calculators.py
#
# Purpose:      A program to allow the user to access two different financial
#               calculators: an investment calculator and a home loan repayment
#               calculator
#
# Author:       Tom Naccarato
#
# Created:      13/05/2022
# ------------------------------------------------------------------------------


# Imports the math package for use of power function
import math

# Asks the user for an input of either loan or investment
print("Please select either \'investment\' or \'bond\' from the menu below to \
proceed:")
calculation_type = input(
    "Would you like to perform an \'investment\' or a \'bond\' calculation?\
\n")
# Makes `calculation_type` lowercase so that case sensitivity doesn't occur
calculation_type = calculation_type.lower()
# Removes whitespace from `calculation_type` to anticipate error
calculation_type = calculation_type.replace(" ", "")


# Decides what calculations the program should run, based on the user's input:

# If investment, ask the user for inputs of:
if calculation_type == "investment":
    # The amount of money that they are depositing
    deposit_amount = float(
        input("How much are you depositing into your account in £?\n"))
    # The interest rate (1)
    interest_rate = float(input("""What is the interest rate of the account?
Please enter the percentage but don't worry about the \'%\' sign! \n"""))
    # Converts `interest_rate` into a percentage by dividing by 100
    interest_rate = interest_rate/100
    # The number of years they plan on investing for
    investment_years = float(
        input("How many years do you plan on investing for?\n"))
    # The type of interest (simple or compound)
    interest = input("Would you like 'compound' or 'simple' interest? \n")
    interest = interest.lower()
    interest = interest.replace(" ", "")

    # Decides what to do based on the type of interest the user selected

    # If simple, calculate total interest using the following formula:
    # deposit_amount(1 + interest_rate x investment_years)
    if interest == "simple":
        total_interest = deposit_amount * \
            (1 + interest_rate * investment_years)
        total_interest = format(total_interest, '.2f')  # Rounds to 2sf
        print("The total in your account with interest will be £{}.".format(
            total_interest))
    # If compound, calculate the total interest using the following formula:
    # deposit_amount(1 + interest_rate) ^ investment_years
    elif interest == "compound":
        total_interest = deposit_amount * \
            math.pow((1+interest_rate), investment_years)
        total_interest = format(total_interest, '.2f')  # Rounds to 2sf
        print("The total in your account with interest will be £{}.".format(
            total_interest))
    # If anything else is selected, print an error message
    else:
        print("""The interest type \'{}\' was not recognised. Please enter
either \'simple\' or \'complex\'.""".format(interest))

# If bond, asks the user for the following inputs:
elif calculation_type == "bond":
    # The present value of the house
    present_value = float(
        input("What is the present value of your house in £? \n"))
    # The interest rate
    interest_rate = float(input("""What is the annual interest rate of the \
account?
Please enter as a percentage but don't worry about the \'%\' sign! \n"""))
    # Converts `interest_rate` into a percentage by dividing by 100
    interest_rate = interest_rate/100
    # Converts `interest_rate` into a monthly amount by dividing by 12
    interest_rate = interest_rate/12
    # The number of months they plan to take to repay the bond
    months_repaying = int(
        input("How many months do you plan to take to repay the bond? \n"))
    # Calculates the amount the user will have to repay each month using the
    # formula:
    # (interest_rate x present_value)/(1-(1+interest_rate)^(-months_repaying))
    repayment = (interest_rate*present_value)/(1-math.pow((1+interest_rate),
                                                          -months_repaying))
    repayment = format(repayment, '.2f')  # Rounds to 2sf
    print("The amount you have to pay back monthly is £{}.".format(repayment))

# If the user enters anything other than investment or bond, give an error
# message
else:
    print("""The calculation type \'{}\' was not recognised. Please enter
either \'investment\' or \'bond\'.""".format(
        calculation_type))

# Keeps terminal open so that final print statement can still be shown (2)
input("Thank you for using our services. Please press enter to quit.")

# References
# (1) For use of multiline strings:
# https://www.techbeamers.com/python-multiline-string/#:~:text=In%20Python%2C%20you%20have%20different,line%20continuation%20character%20in%20Python.

# (2) For keeping terminal open for final print statement:
# https://stackoverflow.com/questions/12375173/how-to-stop-python-closing-immediately-when-executed-in-microsoft-windows
