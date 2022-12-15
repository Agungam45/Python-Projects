import random

random_answer = random.randint(1,100)
guess = int(input("What is your guess? "))
while guess != random_answer:
    if guess > random_answer:
        print("Your guess is too high")
        guess = int(input("What is your guess? "))
    if guess < random_answer:
        print("Your guess is too low")
        guess = int(input("What is your guess? "))
else:
    print("You've got it! The number is", random_answer)
