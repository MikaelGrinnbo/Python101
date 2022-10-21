import random


def main():
    computer_wins  = 0
    player_wins = 0
    isRunning = True

    while isRunning:

        if computer_wins == 3:
            print ("GAME OVER! Computer is the champ!\n")
            isRunning = False
            break
        
        if player_wins == 3:
            print ("GLORIOUS VICTORY! Player wins!\n")
            isRunning = False
            break
        
        computer_move = random.randint(1, 3)

        print ("---------------------------------------")
        print ("ROCK, PAPER, SCICCORS")
        print ("---------------------------------------")
        print (f"Score player: {player_wins}\tComputer: {computer_wins}")
        print ("---------------------------------------")
        print ("Make your choice:")
        print ("1. Rock")
        print ("2. Paper")
        print ("3.Sciccors \n")

        player_move = int( input("Choose move: ") )

        if (computer_move == player_move):  
            print ("Draw, you made the same move. Try again.")

        elif (computer_move == 1 and player_move == 2):
            print ("Player wins, paper beats rock!") 
            player_wins = player_wins + 1

        elif (computer_move == 1 and player_move == 3): 
                print ("Computer wins, rock beats sciccors!") 
                computer_wins = computer_wins + 1
        
        elif (computer_move == 2 and player_move == 1): 
                print ("Computer wins, paper beats rock!") 
                computer_wins = computer_wins + 1

        elif (computer_move ==2 and player_move == 3): 
                print ("Player wins, sciccors beats paper!") 
                player_wins = player_wins + 1

        elif (computer_move == 3 and player_move == 1): 
                print ("Player wins, rock beats scissors!") 
                player_wins = player_wins + 1

        elif (computer_move == 3 and player_move == 2): 
                print ("Computer wins, scissors beats paper!") 
                computer_wins = computer_wins + 1


if __name__ == "__main__":
    main()