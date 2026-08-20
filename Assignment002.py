# =========================================================
# PYTHON FUNDAMENTALS - ASSIGNMENT 02
# Student: Ms. Treasure
# Topics: Lists, Tuples, Sets, Dictionaries, Dictionary Loops,
#         List Operations (len, slicing, append), While Loops
# Theme: Grocery Store
# =========================================================
# Instruction: Complete every task below on your own, in order -
# later tasks build on variables you create in earlier ones.
# If you get stuck, write what you tried as a comment so we can
# review it together next session.
# When done, push this file to your GitHub account.
# =========================================================


# ---------------------------------------------------------
# TASK 1: Store Details (Tuple)
# Instruction: Create a tuple called `store_info` containing
# the store name and its location, e.g. ("FreshMart", "Akure").
# Remember: tuples are ordered but UNCHANGEABLE - this fits
# store details that should never change.
# Print the tuple.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 2: Grocery List (List)
# Instruction: Create a list called `groceries` with AT LEAST
# 5 items (e.g. "bread", "milk", "eggs", "rice", "beans").
# Print the full list.
# Then print how many items are in the list using len().
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 3: Slicing the List
# Instruction: Using slicing (not a loop), print only the
# FIRST 3 items in `groceries`.
# Then print only the LAST 2 items in `groceries`.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 4: Append Operation
# Instruction: Ask the user (using input()) to type ONE new
# item they want to add to the grocery list. Use .append() to
# add it to `groceries`, then print the updated list.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 5: Item Categories (Set)
# Instruction: Create a set called `categories` containing at
# least 4 categories found in a grocery store, e.g.
# {"Fruit", "Dairy", "Grain", "Vegetable"}. Print the set.
# Then check if "Dairy" exists in `categories` using the `in`
# operator and print the result.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 6: Prices (Dictionary)
# Instruction: Create a dictionary called `prices` that maps
# EACH item in your original `groceries` list (from Task 2) to
# a price, e.g. {"bread": 1200, "milk": 900, ...}.
# Print the full dictionary.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 7: Loop Through the Dictionary
# Instruction: Using a for loop and .items(), loop through
# `prices` and print each item together with its price like:
# "bread costs 1200"
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 8: Adding Items to Cart (While Loop)
# Instruction: Ask the user to input how many items they want
# to buy (cast to int) and store it in `num_items`.
# Using a while loop and a counter variable starting at 0,
# print "Item <counter+1> added to cart" for each item, until
# the counter reaches `num_items`.
# Hint: this follows the exact same while loop pattern from
# today's class (start a counter, loop while counter < limit,
# increase the counter by 1 each time).
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 9: Calculating Total (While Loop + List)
# Instruction: Create a list called `cart_prices` with at
# least 4 numbers representing prices, e.g. [1200, 900, 500, 300].
# Using a while loop (counter + len(), just like Task 8), add
# up every price in `cart_prices` into a variable called
# `total`, then print: "Your total is <total>"
# ---------------------------------------------------------



# ---------------------------------------------------------
# BONUS TASK (optional - try only after Tasks 1-9 work):
# Instruction: Look back at Task 4 (list.append) and Task 6
# (dictionary of prices). What do you think would happen if
# you appended a new item to `groceries` but FORGOT to add it
# to `prices` too? Write 2-3 sentences (as a comment) on what
# problem this could cause if you tried to loop through and
# print prices for every item in `groceries`.
# ---------------------------------------------------------
