# Problem Set 1 - B
# =============================================================================
# Write a program that calculates the minimum fixed monthly payment needed in order to pay
# off a credit card balance within 12 months. We will not be dealing with a minimum monthly
# payment rate.

# Take as `raw_input` the following floating point numbers:
# 1) the oustanding balance on the credit card
# 2) annual interest rate as a decimal

# Print out the fixed minimum monthly payment, number of months (at most 12, but possibly
# less) it takes to pay off the debt, and the balance (likely to be a negative number).

# Assume the interest is compounded monthly according to the balance at the start of the month
# (before the payment for the month is made). The monthly payment must be a multiple of $10 and
# is the same for all months. Notice that it is possible for the balance to become negative
# using this payment scheme. In short:

# MONTHLY INTEREST RATE: Annual interest rate / 12.0
# UPDATED BALANCE EACH MONTH: Previous balance * (1 + Monthly Interest Rate) - Minimum monthly payment

# Problem Set 1b
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 40 minutes


def get_input_as_float(msg):
    return float(raw_input(msg))


outstanding_balance_msg = '''
Enter the outstanding balance on your credit card: '''
annual_interest_rate_msg = '''
Enter the annual credit card interest rate as a decimal: '''

init_balance = get_input_as_float(outstanding_balance_msg)
annual_interest_rate = get_input_as_float(annual_interest_rate_msg)

monthly_interest_rate = annual_interest_rate / 12.0

min_monthly_pmt = 0
curr_balance = init_balance

while curr_balance > 0:

    min_monthly_pmt += 10
    curr_balance = init_balance
    total_months = 0

    while total_months < 12 and curr_balance > 0:
        total_months += 1
        interest = monthly_interest_rate * curr_balance
        curr_balance -= min_monthly_pmt
        curr_balance += interest

curr_balance = round(curr_balance, 2)

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(min_monthly_pmt)
print 'Number of months needed: ' + str(total_months)
print 'Balance: ' + str(curr_balance)
