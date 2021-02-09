"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730323863"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
ask: int = randint(1, 100)
print("Your fortune cookie says...")
if ask <= 25:
    print("You will get clapped")
else: 
    if ask > 25 and ask <= 50:
        print("There will be riches coming soon")
    else:
        if ask > 50 and ask < 70:
            print("You will get hit by something soft")
        else:
            print("Congrats on surviving today, try again tomorrow")
print("Now, go spread positive vibes!")