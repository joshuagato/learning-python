# from builtins import input

# name = input("Please enter your name: ")
# age = int(input("How old are you, {0} ? : ".format(name)))

# if age >= 18:
#    print("You are old enough to vote")
#    print("Please put an x in the box")
# else:
#    print("Please come back in {0} years' time.".format(18 - age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print('Please guess higher')
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")

elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

else:
    print("Great!!!! You got it first time.")
