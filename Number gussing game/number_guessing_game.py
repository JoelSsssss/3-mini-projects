import random

print("hello my name is obama")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Type a number larger than 0 next time.')
        quit()
else:
    print('Not a number')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the number")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Not a number')
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("Above set number")
    else:
        print("Below set number")

print("You made", guesses, "guesses")
