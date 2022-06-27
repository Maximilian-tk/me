# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0
    print(f"Actual nunber is {actual_number}")

    while actual_number != guess:
        guess = low + (high - low) // 2 # the maths to each guess, you can use your own maths
        if guess > actual_number: # if the actual number is lower, the high limit becomes the guess
            high = guess - 1 # subtract 1 because the guess itself wasnt the actual number
            tries = tries + 1 # adding 1 try to the try count
        elif guess < actual_number: # if the actual number is higher, the low limit becomes the guess
            low = guess + 1 # add 1 because the guess itself wasnt the actual number
            tries = tries + 1 # adding 1 try to the try count
        print(f"{guess}, {tries} guesses so far") #printing the guess and the number of guesses
    print(f"Correct, {guess} was the number! That took {tries} tries.") # printing statement for the correct guess and number of tries


    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
