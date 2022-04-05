#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user see if grandma approves of them


def main():
    # this function lets the user see if grandma approves of them

    # input
    visual_status = input("Are you attractive (yes/no): ")
    financial_status = input("Are you rich (yes/no): ")

    # process & output
    if visual_status == "yes" or financial_status == "yes":
        print("You can date!")

    elif visual_status == "no" and financial_status == "no":
        print("Ew, get out!")
    else:
        print("Please enter yes or no")

    print("")
    print("Done")


if __name__ == "__main__":
    main()
