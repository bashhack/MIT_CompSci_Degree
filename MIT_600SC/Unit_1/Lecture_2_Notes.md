# MIT 6.00SC - Lecture 2 Notes
# ==========================

* In Python, everything is an object

* Each object has a 'type', which tells us the kind of object it is and what we can do with it

* There are two basic, fundamental categories of types:
  - Scalar (indivisible, the 'atoms' of the programming language)
  - Non-Scalar

* Scalar: int/float, bool, NoneType
* Non-Scalar:

* Expressions - sequence of operands (objects) and operators

* NOTE: Write division as floating point, to avoid the flooring that occurs with int division

* Overloaded operators exist in Python (i.e., +) and have a meaning based on the type
  of the operand(s)

* Variables in Python simply provides a way to name an object

* Assignment then binds a name to an object

* Straight line programs are BORING, and you CANT do much meaningful in one, we
  make interesting programs by introducing decisions

* Branching programs are what make things happen! We can do a lot with them, but
  still nothing truly interesting in the long run.

* Conditionals - if/elif/else (these are the elements of branching programs)

* Programs are meant to be read (this is why Python was designed to be whitespace aware)

* Looping constructs (iteration) are necessary in order to reach Turing completeness

# Check Yourself
# ==========================

1) What is a 'type'?
"A type tells us what kind of object it is, and specifies a series of rules about how that object
can be used."

2) What is an 'expression'?
"An expression is a series of operands and operators. An example might be: variable1 + variable2."

3) What is a type conversion?
"Type convesion or coercion is when an object's type is changed, most often a result of operator
overloading. For example, we might write: 1 + 2 -> 3 or 'a' + 'b' -> 'ab' In each case, the operator
behaves in accordnace with the type of its operands."

4) What is a keyword?
"A keyword is a reserved word in the language, ex. def, and, not - these are part of the syntax."

5) What is the difference between a straight line program and a branching program?
"A straight line program lacks significant decision making - often cited examples include simple
assignments, calculation, or printing of data. Branching programs expand on this by introducing
decision making - either this or that using conditionals. This helps us create more meaningful
programs."

6) What is a conditional?
"Conditionals in the language if/elif/else allow us to create branching programs where an
expression is used to determine the subsequent code to be executed."

# Problem Set 1
# ==========================

1) Write a program to calculate the credit card balance after one year if a person only
   pays the minimum monthly payment required by the credit card company each month.

   Use `raw_input` to ask for the following floating point numbers:
     1) the outstanding balance on the credit card
     2) annual interest rate
     3) minimum monthly payment rate

   For each month, print the minimum monthly payment, remaining balance, principal paid
   in the format shown in the test cases below. All numbers should be rounded to the nearest
   penny. Finally print the result, which should include the total amount paid that year
   and the remaining balance.

   HINTS: Use the round function.

   HINTS: Here's a rough outline:
            Retrieve user input
            Init some state variables. Remember to find the monthly interest rate from the annual
            interest rate taken in as input.
            For each month:
              Compute new balance. This requires computing the minimum monthly payment and figuring
              out how much will be paid to interest and how much will be paid to the principal.
              Update the outstanding balance according to how much principal was paid off.
              Output the minimum monthly payment and the remaining balance.
              Keep track of the total amount of paid over all the past months so far.
              Print out the result statement with the total amount paid and the remaining balance.

    OUTPUT:
    >>>
    Enter the outstanding balance on your credit card: 4800
    Enter the annual credit card interest rate as a decimal: .2
    Enter the minimum monthly payment rate as a decimal: .04
    Month: 1
    Minimum monthly payment: $192.0
    Principle paid: $112.0
    Remaining balance: $4688.0
    Month: 2
    Minimum monthly payment: $187.52
    Principle paid: $109.39
    Remaining balance: $4578.61
    ...

2) Write a program that calculates the minimum fixed monthly payment needed in order to pay
   off a credit card balance within 12 months. We will not be dealing with a minimum monthly
   payment rate.

   Take as `raw_input` the following floating point numbers:
     1) the oustanding balance on the credit card
     2) annual interest rate as a decimal

   Print out the fixed minimum monthly payment, number of months (at most 12, but possibly
   less) it takes to pay off the debt, and the balance (likely to be a negative number).

   Assume the interest is compounded monthly according to the balance at the start of the month
   (before the payment for the month is made). The monthly payment must be a multiple of $10 and
   is the same for all months. Notice that it is possible for the balance to become negative
   using this payment scheme. In short:

   MONTHLY INTEREST RATE: Annual interest rate / 12.0
   UPDATED BALANCE EACH MONTH: Previous balance * (1 + Monthly Interest Rate) - Minimum monthly payment

   HINTS: Start at $10 payments per month and calculate whether the balance will be paid off (taking
   into account the interest accrued each month). If $10 monthly payments are insufficient to pay off
   the debt within a year, increase the monthly payment by $10 and repeat.

NOTE: You'll notice in Problem 2, your monthly payment has to be a multiple of $10.
      Why did we make it that way? In a separate file, you can try changing the code so that the
      payment can be any dollar and cent amount (in other words, the montly payment is a multiple of
      $0.01). Does your code still work? It should, but you may notice your code runs more slowly,
      especially in cases with very large balances and interest rates.

      How can we make this program faster? We can use bisection search (to be covered in lecture 3)!

      We are searching for the smallest monthly payment such that we can pay off the debt within a year.
      What is a reasonable lower bound for this value? We can say $0, but you can do better than that.
      If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the
      original balance, so we must pay at least this much. One-twlefth of the original balance is a good
      lower bound.

      What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire
      balance at the end of the year. What we ultimately pay must be greater than what we wouldn've paid
      in monthly installments, because the interest was compounded on the balance we didn't pay
      off each month. So a good upper bound would be one-twelfth of the balance, after having its
      interested compounded monthly for an entire year.

      In short:
      MONTHLY PAYMENT LOWER BOUND: Balance / 12.0
      MONTHLY PAYMENT UPPER BOUND: (Balance * (1 + (Annual interest rate / 12.0)) ** 12.0) / 12.0

      OUTPUT:
      >>>
      Enter the outstanding balance on your credit card: 1200
      Enter the annual credit card interest rate as a decimal: .18
      RESULT
      Monthly payment to pay off debt in 1 year: 120
      Number of months needed: 11
      Balance: -10.05
      >>>
      Enter the outstanding balance on your credit card: 32000
      Enter the annual credit card interest rate as a decimal: .2
      RESULT
      Monthly payment to pay off debt in 1 year: 2970
      Number of months needed: 12
      Balance: -74.98


3) Write a program that uses these bounds and bisection search
  (for more info check here: https://en.wikipedia.org/wiki/Bisection_method) to find the
  smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt
  within a year. Try it out with large inputs, and notice how fast it is. Produce the output in the same format
  as you did in Problem 2.

NOTE: Programs must be saved as ps1a.py, ps1b.py, and ps1c.py
      At top of programs, please include:
      # Problem Set 1
      # Name:
      # Collaborators:
      # Time Spent:


1) COMPLETED - See ./ps1a.py
2) COMPLETED - See ./ps1b.py
3) COMPLETED - See ./ps1c.py
