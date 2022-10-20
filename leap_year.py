#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 20th 2022
# Tells the user if the year they
# input is a leap year or not


def main():

    # Determining whether the user can date their grandchild
    try:
        # Getting the Users age
        user_input_as_string = input("Input a year: ")
        user_input_as_int = int(user_input_as_string)
    except Exception:
        print("Invalid input, please input a year")

    # Determine whether the user is the right age to date the grandchild
    else:
        if user_input_as_int % 4 == 0:
            if user_input_as_int % 100 == 0 and user_input_as_int % 400 == 0:
                print("It is a leap year!")
        else:
            print("It is not a leap year.")

    finally:
        print("Done")


if __name__ == "__main__":
    main()
