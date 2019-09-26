import random

print("==================")
print(" GUESS MY NUMBER   ")
print("By Collin Freeland  ")
print("==================")
print ("")
name = input("What's your name? ")
print("")
if name == ("Creeper"):
    print (f"Aww man!")
if name == ("Jotaro"):
    print (f"Yare Yare Daze")
if name == ("Kars"):
    print (f"https://www.youtube.com/watch?v=XUhVCoTsBaM")
if name == ("Wammu"):
    print (f"https://www.youtube.com/watch?v=XUhVCoTsBaM")
if name == ("Esidsi"):
    print (f"https://www.youtube.com/watch?v=XUhVCoTsBaM")
if name == ("Dio"):
    print (f"WRYYYYYYYYYYYYYYYYYYYYYY")
if name == ("the_number"):
    print (f"Tsk. Tsk. Tsk. No cheating!")
print("")

the_number = random.randint(0,100)
print ("I'm thinking of an integer between 0 and 100. Can you guess it?")
print("")

guess = -1

while guess !=the_number:
    guess_text= input("What is your guess? ")
    guess = int(guess_text)
    print("")

    if guess < the_number:
        print(f"Sorry, {name}, but your guess is too LOW. Try again.")
    elif guess > 101:
        print(f"Seriously? I gave you 0 to 100, {name}. I didn't code this for nothing, you know.")
    elif guess > the_number:
        print(f"Sorry, {name}, but your guess is too HIGH. Try again.")
    else:
        print(f"You guessed it! Congratulations, {name}!")