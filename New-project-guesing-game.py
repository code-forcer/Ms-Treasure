import random

# The computer picks a number between 1 and 10
secret_number = random.randint(1, 10)
guess = 0

print("I am thinking of a number between 1 and 10!")

# Keep asking until the user gets it right
while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")
