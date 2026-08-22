# =========================================================
# PYTHON FUNDAMENTALS - ASSIGNMENT 03
# Student: Ms. Treasure
# Topics: Functions, Parameters, Return Values,
#         Calling One Function From Another
# Theme: Library Membership & Book Borrowing System
# =========================================================
# Instruction: Complete every task in order - each function
# builds on the one before it, just like register_user() and
# login() did in class. Define every function first, then
# only call main() at the very bottom, exactly like the class
# example did.
# When done, push this file to your GitHub account.
# =========================================================


# ---------------------------------------------------------
# TASK 1: welcome_message()
# Instruction: Define a function called `welcome_message`
# that takes NO parameters. It should print:
# "Welcome to Codeforcer Library. Please register to continue."
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 2: register_member()
# Instruction: Define a function called `register_member`
# that takes NO parameters.
# Inside it:
#   - Ask the user to input their name and email.
#   - If '@' is NOT in the email, print "Invalid email" and
#     return None, None (registration stops here).
#   - Otherwise, print "Registration successful" and
#     return the name and email (two values).
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 3: borrow_book(name)
# Instruction: Define a function called `borrow_book` that
# takes ONE parameter: `name`.
# Inside it:
#   - Ask the user to input the title of the book they want
#     to borrow.
#   - Print: "<name> has borrowed <book title>"
#   - Return the book title.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 4: return_book(name, book)
# Instruction: Define a function called `return_book` that
# takes TWO parameters: `name` and `book`.
# Inside it:
#   - Print: "<name> has returned <book>. Thank you!"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 5: is_book_available(book, borrowed_books)
# Instruction: Define a function called `is_book_available`
# that takes TWO parameters: `book` (a string) and
# `borrowed_books` (a list of book titles already borrowed
# by others).
# Inside it:
#   - Use the `in` operator to check if `book` is already in
#     `borrowed_books`.
#   - Return True if it is available (NOT in the list),
#     or False if it is already borrowed (already in the list).
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 6: main()
# Instruction: Define a function called `main` that takes NO
# parameters. Inside it, in this order:
#   1. Call welcome_message()
#   2. Call register_member() and store the two returned
#      values in variables `name` and `email`.
#   3. Create a list called `borrowed_books` with 2-3 book
#      titles already in it (pretend other members borrowed
#      them), e.g. ["Things Fall Apart", "Half of a Yellow Sun"]
#   4. Call borrow_book(name) and store the returned value in
#      a variable called `book`.
#   5. Call is_book_available(book, borrowed_books) and store
#      the result in a variable called `available`.
#   6. If `available` is True, print "You may keep the book."
#      If False, print "Sorry, that book is currently unavailable."
#   7. Ask the user (input) if they want to return the book now
#      ("yes"/"no"). If yes, call return_book(name, book).
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 7: Run the Program
# Instruction: Just like the class example ended with main(),
# call main() here at the very bottom of the file so the whole
# program runs.
# ---------------------------------------------------------



# ---------------------------------------------------------
# BONUS TASK (optional - try only after Tasks 1-7 work):
# Instruction: In Task 2, register_member() RETURNS the name
# and email instead of just printing them. Write 2-3 sentences
# (as a comment) on why returning the values and passing them
# into borrow_book(name) is more useful than register_member()
# printing the name and borrow_book() asking the user to type
# their name again.
# ---------------------------------------------------------
