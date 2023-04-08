import random

secret_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while attempts < 10:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number in", attempts + 1, "attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts += 1

if attempts == 10:
    print("Sorry, you didn't guess the number. The number was", secret_number)
