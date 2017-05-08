# Problem Set 1 - C
# =============================================================================
# Write a program that uses these bounds and bisection search
# (for more info check here: https://en.wikipedia.org/wiki/Bisection_method) to find the
# smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt
# within a year. Try it out with large inputs, and notice how fast it is. Produce the output in the same format
# as you did in Problem 2.

# Problem Set 1c
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 2 hours 30 minutes


def get_input_as_float(msg):
    return float(raw_input(msg))


outstanding_balance_msg = '''
Enter the outstanding balance on your credit card: '''
annual_interest_rate_msg = '''
Enter the annual credit card interest rate as a decimal: '''

init_balance = get_input_as_float(outstanding_balance_msg)
annual_interest_rate = get_input_as_float(annual_interest_rate_msg)

balance = init_balance
lower_bound = init_balance / 12.0
upper_bound = (init_balance * (1 + (annual_interest_rate / 12.0)) ** 12.0) / 12.0

while True:
    balance = init_balance
    monthly_pmt = (lower_bound + upper_bound) / 2

    for m in range(1, 13):
        monthly_interest = round(balance * annual_interest_rate / 12, 2)
        balance += monthly_interest - monthly_pmt
        if balance <= 0:
            break

    if (upper_bound - lower_bound < .005):
        # Bisection search space is small enough
        print 'RESULT'

        print 'monthly interest: ', monthly_interest
        print 'balance: ', balance

        # Round monthly payment up to the nearest cent
        monthly_pmt = round(monthly_pmt + .0049, 2)
        print 'Monthly payment to pay off debt in 1 year: $' + str(monthly_pmt)

        balance = init_balance

        for m in range(1, 13):
            monthly_interest = round(balance * annual_interest_rate / 12, 2)
            balance += monthly_interest - monthly_pmt
            if balance <= 0:
                break
        print 'Number of months needed: ' + str(m)
        print 'Balance: $' + str(round(balance, 2))
        break
    elif (balance < 0):
        # paid too much
        upper_bound = monthly_pmt
    else:
        # paid too little
        lower_bound = monthly_pmt
