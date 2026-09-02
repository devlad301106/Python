import random

num = random.randint(1,10)
tries = 0

while True:
    guess = int(input("Guess your number from 1 to 10: "))

    if guess == num:
        print("You are right!")
        break

    elif guess < num:
        print("Guess higher!")
        tries += 1

    elif guess > num:
        print("Guess lower!")
        tries += 1

    else:
        tries += 1
        print("Guess a number!")

print(f"Congrats! You guessed right in {tries} tries.")
