# =========================================================
# PYTHON FUNDAMENTALS - ASSIGNMENT 04
# Student: Ms. Treasure
# Topics: OOP (Classes, __init__, self, methods), the math
#         module, keyword arguments, loops over lists applying
#         a formula, formula-based programs
# =========================================================
# Instruction: Complete every section in order. Sections are
# independent of each other, just like today's class covered
# separate ideas (the Dog class, the math module, the linear
# model, the quadratic formula).
# When done, push this file to your GitHub account.
# =========================================================


# =========================================================
# SECTION A: OOP - The Car Class
# =========================================================

# ---------------------------------------------------------
# TASK 1: Define the Car class
# Instruction: Just like the Dog class in today's notes,
# define a class called `Car` with a constructor (__init__)
# that takes `self`, `brand`, and `year`, and stores them as
# self.brand and self.year.
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 2: Add methods to Car
# Instruction: Inside the Car class, add these 3 methods
# (each takes only `self`):
#   - start_engine(self)  -> returns f"{self.brand}'s engine has started."
#   - honk(self)           -> returns f"{self.brand} says Beep beep!"
#   - describe(self)       -> returns f"This is a {self.year} {self.brand}."
# ---------------------------------------------------------



# ---------------------------------------------------------
# TASK 3: Create an object and use it
# Instruction: Create a Car object called `my_car` with any
# brand and year you like. Then:
#   - print(my_car.brand)
#   - print(my_car.year)
#   - print(my_car.describe())
#   - print(my_car.start_engine())
#   - print(my_car.honk())
# ---------------------------------------------------------



# =========================================================
# SECTION B: The math Module
# =========================================================

# ---------------------------------------------------------
# TASK 4: Pythagorean Theorem
# Instruction: from math import sqrt, pow (just like class).
# Ask the user to input the two shorter sides of a right
# triangle (side_a, side_b), cast to float.
# Calculate the hypotenuse using: sqrt(pow(side_a, 2) + pow(side_b, 2))
# Print the result formatted to 2 decimal places, e.g.:
# "The hypotenuse is 5.00"
# ---------------------------------------------------------



# =========================================================
# SECTION C: Functions with Keyword Arguments
# =========================================================

# ---------------------------------------------------------
# TASK 5: rectangle_area(length, breadth)
# Instruction: Define a function called `rectangle_area` that
# takes two parameters: `length` and `breadth`, and returns
# their product.
# Then call it the SAME way power_func() was called in class -
# using keyword arguments straight from input(), e.g.:
# print(rectangle_area(length=float(input("Enter length: ")), breadth=float(input("Enter breadth: "))))
# ---------------------------------------------------------



# =========================================================
# SECTION D: Applying a Formula Across a List
# =========================================================

# ---------------------------------------------------------
# TASK 6: Your Own Linear Model
# Instruction: Just like the y = mx + c example in class,
# create a list called `x_values` with 5 numbers of your choice.
# Choose YOUR OWN values for `m` (slope) and `c` (intercept) -
# do not reuse m=2, c=-2 from class.
# Using a for loop, calculate y = (m * x) + c for every value
# in x_values, and print:
# "when x = <x> then y = <y>"
# ---------------------------------------------------------



# =========================================================
# SECTION E: A New Formula-Based Program
# =========================================================

# ---------------------------------------------------------
# TASK 7: Distance Between Two Points
# Instruction: This uses the same sqrt/pow idea as the
# quadratic formula program in class, applied to a new formula.
# Ask the user to input 4 numbers: x1, y1, x2, y2 (all floats).
# Calculate the distance between point (x1, y1) and point
# (x2, y2) using:
#   distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
# Print the result formatted to 2 decimal places, e.g.:
# "The distance between the two points is 7.07"
# ---------------------------------------------------------



# ---------------------------------------------------------
# BONUS TASK (optional - try only after Tasks 1-7 work):
# Instruction: Add ONE more method to your Car class from
# Section A, called `fuel_needed(self, distance, consumption)`,
# where `consumption` is km-per-litre. It should return
# distance / consumption (how many litres of fuel are needed).
# Call it on `my_car` with any distance and consumption you like.
# ---------------------------------------------------------
