#randomizer game
import random

my_number = random.randint(1,10)

user_guess = int(input("I am thinking of a number between 1 - 5, guess!\n"))

while user_guess != my_number:
    if user_guess < my_number:
        print ("your guess is lower than the number")
    elif user_guess > my_number:
        print("your guess is higher than the number")
    user_guess= int(input("guess again "))

print("woho you got it")
print(my_number)
