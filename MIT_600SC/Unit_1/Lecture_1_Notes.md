# MIT 6.00SC - Lecture 1 Notes
# ==========================

* Declarative vs Imperative Knowledge
  - Declarative knowledge is composed of facts
  - Imperative knowledge tells us the steps to accomplish something, i.e., a recipe

* Algorithm - how to perform a computation
  Qualities of:
    - Converged
    - Instructions
    - Flow of control
    - Termination condition

* History of Computing:
  - Earliest computers were designed to perform fixed programs
  - Linear equation problem solving led to one of the earliest computers,
    figured out artillery projectile path
  - The stored program computer brought computing into the everyday,
    instructions are the same as data - no distinction between the program and the data
  - At that point, computers could produce their own programs
  - Conceptually, the idea of the computer being the program itself led to the invention
    of the interpreter - can (theoretically) perform anything you can describe or do with a computer

                                                  Memory
                  ^                                                          ^
                  |  |                                                       |   |
                     v                                                           v
     Control Unit (i.e., tells it what to do)   < ---------- >   Arithmetic Logic Unit (the 'brains', does computation)
                                                                         [ accumulator (stores results)]
                                                                                    /       \
                                                                                 Input      Output (how we interact with the computer)

* All programming languages have a syntax, static semantics, semantics:
  - syntax: tells us which seqs of chars, symbols constitute a well-formed string
  - static semantics: which well-formed strings have a meaning
  - semantics: what the meaning is

* Compiled vs Interpreted
  - Interpreter: source code => checker => interpreter => output
  - Compiled: source code => checker/compiler => object code => interpreter => output

* Errors:
  - crash
  - never stop - infinite loop
  - run to completion, but return the wrong answer


# Check Yourself
# ==========================

1) What is the difference between declarative and imperative knowledge?
"We say that declarative knowledge is composed of facts about a thing, whereas
imperative knowledge is composed of instructions to accomplish a task."

2) What is the advantage of a stored-program computer?
"The earliest computers were fixed-program entities, designed to do
one thing well and only that thing. The stored-program computer brought about
the ability for the computer to run multiple programs, because the instructions
were the same as data, data the same as instructions."

3) What are the syntax, static semantics, and semantics of a language?
"We describe syntax as the rules that define a well-formed string, the static
semantics as the rules that define whether a well-formed string has meaning,
and the semantics as the meaning, itself."

4) What sorts of errors can occur in a program?
"We have the following general errors (in rough order of severity):
 - crashes
 - infinite loops
 - program completion but with incorrect answer"


# Problem Sets
# ==========================
1) Install Python
2) Write a program, 'Entering and Printing Your Name':
   a) MUST ask the user to enter his/her birthdate
   b) MUST ask the user to enter his/her last name
   c) MUST print out the last name, and date of birth, in that order

1) COMPLETED
2) COMPLETED - See: ./ps0.py
