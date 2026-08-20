# =========================================================
# PYTHON FUNDAMENTALS - CLASSWORK 03
# Student: Ms. Treasure
# Topics: Input/Output (IO), Type Casting, Conditionals (if/elif/else)
# Theme: Simple Banking System
# =========================================================
# This is ONE program built step by step, just like the
# calculator you just solved. Follow each instruction in
# order and write your code directly under it - by the end
# you will have a working mini banking system.
# Run the file after each task to check it works before moving on.
# =========================================================


# ---------------------------------------------------------
# TASK 1: Welcome & Starting Balance
# Instruction: Ask the user to input their account balance
# (remember: input() always returns a string, so cast it to
# a float). Store it in a variable called `balance`.
# Then print: "Welcome! Your current balance is <balance>"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 2: Show the Menu
# Instruction: Using print statements (just like the
# calculator menu), display these 4 options to the user:
#   Enter 1 for Deposit
#   Enter 2 for Withdraw
#   Enter 3 for Check Balance
#   Enter 4 for Exit
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 3: Get the User's Choice
# Instruction: Ask the user to input which operation they
# want to perform (cast it to int). Store it in a variable
# called `operation`.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 4: Deposit (operation == 1)
# Instruction: Start your if/elif/else chain here.
# If operation == 1:
#   - Ask the user to input the amount they want to deposit
#     (cast to float).
#   - Add it to `balance`.
#   - Print: "Deposit successful. Your new balance is <balance>"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 5: Withdraw (operation == 2)
# Instruction: elif operation == 2:
#   - Ask the user to input the amount they want to withdraw
#     (cast to float).
#   - IMPORTANT: check if the withdrawal amount is GREATER
#     than the balance first.
#       - If it is, print "Insufficient funds. Your balance
#         is <balance>" (do NOT subtract anything).
#       - Otherwise, subtract it from `balance` and print
#         "Withdrawal successful. Your new balance is <balance>"
#   Hint: this needs a nested if/else INSIDE this elif.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 6: Check Balance (operation == 3)
# Instruction: elif operation == 3:
#   - Simply print: "Your current balance is <balance>"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 7: Exit (operation == 4)
# Instruction: elif operation == 4:
#   - Print: "Thank you for banking with us. Goodbye!"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 8: Invalid Operation
# Instruction: else:
#   - Print: "Invalid operation. Please enter a number
#     between 1 and 4."
# ---------------------------------------------------------



# ---------------------------------------------------------
# BONUS TASK (optional - try only after Tasks 1-8 work):
# Instruction: What do you think would happen if the user
# ran the program again and wanted to make ANOTHER
# transaction without restarting the program? Write 2-3
# sentences (as a comment) on what you think is missing,
# and why the program currently only allows ONE transaction
# before it ends. We will cover the fix for this soon.
# ---------------------------------------------------------
