import math
from banner import banner

banner("PYTHAGOREAN CALCULATOR", "Collin Freeland")

# 1. Display Banner
# 2. Display Pythagorean theorem and get the user's input for side length
# 3. If the user has not entered one side of a triangle, tell them the length of that missing side
# 4. Ask the user if they would like to solve another problem.
# __name__ == "__main__"

print("Welcome to The Pythagorean Calculator! We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")

try_again = "Y"

while try_again == "Y":

    print("")
    print("Please enter the length of each side, or leave it blank if you don't know.")

    a = input("a = ")
    b = input("b = ")
    c = input("c = ")


    if a == "":
        b = float(b)
        c = float(c)
        input_a = math.sqrt((c*c) - (b*b))
        print(f"Your missing side is a, and it's length is {input_a}\n")


    elif b == "":
        c = float(c)
        a = float(a)
        input_b = math.sqrt((c*c) - (a*a))
        print(f"Your missing side is b, and it's length is {input_b}\n")

    elif c == "":
        a = float(a)
        b = float(b)
        input_c = math.sqrt((a*a) + (b*b))
        print(f"Your missing side is c, and it's length is {input_c}\n")


    try_again = input("Would you like to try again? [Y/N] ")
    if try_again == "Y":
        pass
    elif try_again == "N":
        print('')
        print("Thank you for using the Pythagorean Calculator.")
    else:
        print('')
        print("I'm going to assume you mean No.")