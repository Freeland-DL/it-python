from banner import banner
import random

banner ("ROCK, PAPER, SCISSORS", "Collin Freeland")

print("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner.")
print('')

pscore = int(0)


cscore = int(0)

response = 'Y'

while response == "Y":
    pscore = int(0)
    cscore = int(0)
    while pscore < 3 and cscore < 3:
        comp_choice = random.randint(1, 3)

        print(f'SCORE: Player: {pscore} Computer: {cscore}')
        print('')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('')
        player_choice = int(input('What is your choice? [Number] '))
        print("")

        if player_choice == 1:
            if comp_choice == 1:
                print('You chose Rock, and the computer chose Rock. It is a tie.')
            elif comp_choice == 2:
                print('You chose Rock, and the computer chose Paper. The computer wins this round.')
                cscore = cscore + 1
            else:
                print('You chose Rock, and the computer chose Scissors. You win this round.')
                pscore = pscore +1
        elif player_choice == 2:
            if comp_choice == 1:
                print('You chose Paper, and the computer chose Rock. You win this round ')
                pscore = pscore +1
            elif comp_choice == 2:
                print('You chose Paper, and the computer chose Paper. It is a tie.')
            else:
                print('You chose Paper, and the computer chose Scissors. The computer wins this round.')
                cscore = cscore + 1
        elif player_choice == 3:
            if comp_choice == 1:
                print('You chose Scissors, and the computer chose Rock. The computer wins this round.')
                cscore = cscore + 1
            elif comp_choice == 2:
                print('You chose Scissors, and the computer chose Paper. You win this round.')
                pscore = pscore +1
            else:
                print('You chose Scissors, and the Computer chose Scissors. It is a tie')
        else:
            print('That was not an option, please try again.')

    if pscore >= 3:
        print("")
        print("You have defeated the computer in an honorable battle! It was hubris for he computer to think it could win against such a formidable opponent. Congratulations!")
    elif cscore >= 3:
        print("")
        print("Congratulations, you let a computer beat you. It was my understanding that humans were far superior to them. I guess I was wrong.")

    print('')


    response = input("Would you like to try again? [Y/N] ")
    if response.upper() == "Y":
        pass
    elif response == "N":
        print('')
        print("Very well, I hope you enjoyed your battle.")
    else:
        print('')
        print("I'm going to assume you mean No.")