# Entering and Printing Your Name
# =============================================================================
# a) MUST ask the user to enter his/her birthdate
# b) MUST ask the user to enter his/her last name
# c) MUST print out the last name, and date of birth, in that order


# Problem Set 0
# Name: Marc Laughton
# Collaborators: N/A
# Time Spent: 5 minutes


dob_msg = 'What is your date of birth (e.x. 1/1/1111)? '
last_name_msg = 'What is your last name? '


def get_input(msg):
    return raw_input(msg)


dob = get_input(dob_msg)
last_name = get_input(last_name_msg)

print last_name, dob
