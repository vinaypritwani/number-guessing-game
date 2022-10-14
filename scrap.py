n = 18
number_of_guesses = 1
print("no of guessses is only upto 9 times")
while(number_of_guesses<=9):
    a = int(input("enter your number here: " ))
    if a < 18:
        print("you have entered a smaller number")
    elif a > 18:
        print("you have entered a bigger number")
    else:
        print("you won the game")
        print(number_of_guesses,"no of guesses he took to finish")
        break
    print(9-number_of_guesses,"no of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses>9):
    print("GAME OVER")

