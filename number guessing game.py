import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
