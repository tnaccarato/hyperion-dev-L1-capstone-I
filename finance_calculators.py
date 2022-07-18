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
# Importing Libraries

# Imports the math package for use of power function
import math
# Imports the tkinter package for UI
import tkinter as tk
from tkinter import Toplevel, ttk
# ------------------------------------------------------------------------------
# Defining Functions


def simple_interest(deposit_amount, interest_rate, investment_years):
    '''Calculates simple interest'''
    global window_width, window_height, center_x, center_y
    simple_window = Toplevel(root)
    simple_window.title("Simple Interest Result")
    simple_window.geometry(f'{window_width}x{window_height}+{center_x}+\
                           {center_y}')
    # Converts interest rate to percentage
    interest_rate = interest_rate/100
    # Calculates total interest
    total_interest = deposit_amount * \
    (1 + interest_rate * investment_years)
    total_interest = format(total_interest, '.2f')
    # Displays a label with the total interest
    ttk.Label(simple_window, text=f"The total in your account with interest \
will be £{total_interest}").pack()


def compound_interest(deposit_amount, interest_rate, investment_years):
    '''Calculates compound interest'''
    global window_width, window_height, center_x, center_y
    compound_window = Toplevel(root)
    compound_window.title("Compound Interest Result")
    compound_window.geometry(f'{window_width}x{window_height}+{center_x}+\
        {center_y}')
    # Converts interest rate to percentage
    interest_rate = interest_rate/100
    # Calculates total interest
    total_interest = deposit_amount * \
        math.pow((1+interest_rate), investment_years)
    total_interest = format(total_interest, '.2f')  # Rounds to 2sf
    # Displays a label with the total interest
    ttk.Label(compound_window, text=f"The total in your account with interest \
will be £{total_interest}").pack()


def investment_click():
    '''Displays functions for investment calculation'''
    # Creates a new window if investment is clicked
    global window_width, window_height, center_x, center_y
    investment_window = Toplevel(root)
    investment_window.title("Investment")
    window_height = 300
    window_width = 400
    investment_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # Asks user for inputs of:
    # Deposit amount
    menu_text = ttk.Label(investment_window, text="How much are you depositing \
into your account in £?").pack()
    deposit_amount = tk.StringVar(investment_window, "0")
    ttk.Entry(investment_window, textvariable=deposit_amount).pack()
    # Interest rate
    menu_text = ttk.Label(investment_window, text="What is the interest rate \
of the account?\
 Please enter the percentage but don't worry about the \'%\' sign!").pack()
    interest_rate = tk.StringVar(investment_window, "0")
    ttk.Entry(investment_window, textvariable=interest_rate).pack()
    # How many years they are investing for
    menu_text = ttk.Label(investment_window, text="How many years are you \
investing for?").pack()
    investment_years = tk.StringVar(investment_window, "0")
    ttk.Entry(investment_window, textvariable=investment_years).pack()
    # The type of interest
    menu_text = ttk.Label(investment_window, text="What type of interest \
calculation would you like to perform?").pack()
    # Button for simple interest
    simple_button = ttk.Button(investment_window, text="Simple",
        command= lambda: simple_interest(float(deposit_amount.get()),
            float(interest_rate.get()),
                float(investment_years.get()))).pack()
    # Button for compound interest
    compound_button = ttk.Button(investment_window, text="Compound",
        command=lambda: simple_interest(float(deposit_amount.get()),
            float(interest_rate.get()),
                float(investment_years.get()))).pack()
# ------------------------------------------------------------------------------


# Creates UI window
root = tk.Tk()
root.title("Financial Calculator")
# Sets the window size
window_width = 400
window_height = 200
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Creates a label widget for the main menu text
ttk.Label(root, text="Please select either \'investment\' or \
\'bond\' from the menu \nbelow to proceed:", anchor="center",
                      justify="center").pack()

# Creates buttons for selecting investment or bond
investment_button = ttk.Button(root, text="Investment",
                               command=investment_click).pack()

root.mainloop()

bond_button = ttk.Button(root, text="Bond", command=bond_click()).pack()




# Decides what to do based on the type of interest the user selected

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




# References
# (1) For use of multiline strings:
# https://www.techbeamers.com/python-multiline-string/#:~:text=In%20Python%2C%20you%20have%20different,line%20continuation%20character%20in%20Python.

# (2) For keeping terminal open for final print statement:
# https://stackoverflow.com/questions/12375173/how-to-stop-python-closing-immediately-when-executed-in-microsoft-windows
