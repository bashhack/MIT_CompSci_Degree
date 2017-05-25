# Problem Set 1 - A
# =============================================================================
# Write a program to calculate the credit card balance after one year if a
# person only pays the minimum monthly payment required by the credit card
# company each month.

# Use `raw_input` to ask for the following floating point numbers:
# 1) the outstanding balance on the credit card
# 2) annual interest rate
# 3) minimum monthly payment rate

# For each month, print the minimum monthly payment, remaining balance,
# principal paid in the format shown in the test cases below. All numbers
# should be rounded to the nearest penny. Finally print the result, which
# should include the total amount paid that year and the remaining balance.

# Problem Set 1a
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 20 minutes


def get_input_as_float(msg):
    return float(raw_input(msg))


outstanding_balance_msg = '''
Enter the outstanding balance on your credit card: '''
annual_interest_rate_msg = '''
Enter the annual credit card interest rate as a decimal: '''
min_monthly_rate_msg = '''
Enter the minimum monthly payment rate as a decimal: '''

curr_balance = get_input_as_float(outstanding_balance_msg)
annual_interest_rate = get_input_as_float(annual_interest_rate_msg)
min_monthly_rate = get_input_as_float(min_monthly_rate_msg)

monthly_interest_rate = annual_interest_rate / 12.0

totalPaid = 0

for m in range(1, 13):
    min_monthly_pmt = round(min_monthly_rate * curr_balance, 2)
    totalPaid += min_monthly_pmt
    monthly_interest_paid = round(monthly_interest_rate * curr_balance, 2)
    principal_paid = min_monthly_pmt - monthly_interest_paid
    curr_balance -= principal_paid

    print 'Month: ' + str(m)
    print 'Minimum monthly payment: $' + str(min_monthly_pmt)
    print 'Principal_paid: $' + str(principal_paid)
    print 'Remaining balance: $' + str(curr_balance)

print 'RESULT'
print 'Total amount paid: $' + str(totalPaid)
print 'Remaining balance: $' + str(curr_balance)
