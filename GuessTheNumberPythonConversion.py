import random

def main():

     randomTall = random.randint(1, 10)


     numberOfGuesses = 1

     isRunning = True
     print ("Guess a number between 1 and 10")
     
     Guess = int( input("Guess: ") )

     while (isRunning):
        if (numberOfGuesses < 3):
           

          if (Guess == randomTall):
            print ("You guessed right!")
            isRunning = False
            
          elif ( Guess < randomTall):
            numberOfGuesses = numberOfGuesses + 1
            print ("You guessed too low")
            print ("Guess again")
            Guess = int( input("Guess: ") )
        
          elif (Guess > randomTall):
            numberOfGuesses = numberOfGuesses + 1
            print ("You guessed too high")
            print ("Guess again")
            Guess = int( input("Guess a number: ") )

        else:
          print ("You have guessed wrong too many times")
          print ("GAME OVER")
          isRunning = False

main()