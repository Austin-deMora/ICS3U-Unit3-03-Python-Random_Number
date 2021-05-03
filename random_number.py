#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: April 2021
# This program checks if a person chose the right number between 0 and 9

import random


def main():
    # This function checks if the person chose right or wrong

    # Input

    chosen_number = int(input("Enter a number between 0 and 9: "))
    generated_number = random.randint(0, 9)  # A number between 0 and 9
    print("")

    # process
    if chosen_number == generated_number:
        # Output
        print("Correct!")

    else:
        print("The correct number is {}".format(generated_number))


if __name__ == "__main__":
    main()
