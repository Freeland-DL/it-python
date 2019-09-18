from banner import banner

banner ("ZIP CODE SORTER", "Collin Freeland")

#1. Get zipcode from the user
#2. Read the zipcode, and pin it to the corresponding city
#3. Print the zipcode and what city it belongs to
#4. Ask the user if they want to enter another zip code
#5. If yes, return to 1. If no, print goodbye message.

print("Welcome to the Newaygo County zip code sorter.")
print("")

response = 'Y'

while response == "Y":

    zipcode = input("Please enter a zip code: ")
    print("")
    if zipcode == "49412":
        print(f"The zip code {zipcode} is for Fremont")
        print("")
    elif zipcode == "49309":
        print(f"The zip code {zipcode} is for Bitely")
        print("")
    elif zipcode == "49312":
        print(f"The zip code {zipcode} is for Brohman")
        print("")
    elif zipcode == "49337":
        print(f"The zip code {zipcode} is for Croton and Newaygo")
        print("")
    elif zipcode == "49413":
        print(f"The zip code {zipcode} is for Fremont")
        print("")
    elif zipcode == "49327":
        print(f"The zip code {zipcode} is for Grant")
        print("")
    elif zipcode == "49349":
        print(f"The zip code {zipcode} is for White Cloud")
        print("")
    else:
        print(f"The zip code {zipcode} is not in Newaygo County.")
        print("")

    response = input("Would you like to enter another zip code? [Y/N] ")
    print("")
    if response == "Y":
        pass
    elif response == "N":
        print("Thank you for using the Newaygo County zip code sorter. Goodbye!")
    else:
        print("Did you mean no..?")