"""An exercise in remainders and boolean logic."""

__author__ = "730323863"


# Begin your solution here...
ask: int = int(input("Enter a number:"))
if ask % 7 == 0 and ask % 2 == 0:
    print("TAR HEELS")
else:  
    if ask % 7 == 0:
        print("HEELS")
    else:
        if ask % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")