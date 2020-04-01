i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

# print()
# print()
#
# available_exits = ["east", "north east", "south"]
# chosen_exit = ''
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# print("Aren't you glad you got of there!")


print()
print()

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0   # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())

    # if guess != answer:
    if guess < answer:
        print("Please guess higher: ")
    elif guess > answer:
        print("Please guess lower: ")
    else:
        print("Well done, you guessed it")
    # else:
    #     print("Great!!! You got it right right at the very first time.")

# You can widen the range of the random numbers to like 1000
# and make sure the user cannot try more than 10 guesses.
# Also, if the user is able to guess right just at the first time,
# he should be rewarded with some kind words