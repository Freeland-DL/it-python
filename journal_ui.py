import journal
from banner import banner

banner("DEEP THOUGHTS", "Collin Freeland")

def main():
    run_event_loop()

def run_event_loop():
    filename = input("What file would you like to load? ")
    journal_data = journal.load(filename)  # []

    while True:
        command = input("[L]ist entries, [A]dd an entry, E[x]it, [D]elete a file: ")
        print("")

        if command.upper() == "L":
            list_entries(journal_data)
            print("")
        elif command.upper() == "A":
            add_entry(journal_data)
            print("")
        elif command.upper() == "X":
            break
        elif command.upper() == "D":
            print("")
        else:
            print("Sorry, that wasn't an avaliable command")
            print("")
    journal.save(filename, journal_data)

def list_entries(data):
    print("Your Journal Entries: ")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")

def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    # data.append(entry)


main()