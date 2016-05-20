#File:guess86448.py
#Author:Simmy Payyappilly Varghese,Student ID:86448
#Date Created:03/30/2015
"""This Program implements a number guessing game.

   In Each game,using random module a random number is generated.User is prompted to enter a number between 0 and 12.If user input matches with random number,
   prints message that user has correct guess and new game starts.If user enter wrong number,displays message that user made wrong guess.User will be given four chances.
   After fourth,new game starts.User should enter'X' to exit the game and program will give a game summary of total games,total wins and losses
"""

import random
def main():
    print("Welcome to the number guessing game.")
    print("For each game, you have 4 chances to guess a secret number from 1 to 12.")
    gameCount=0                                                                  #gameCount-number of games user played
    winCount=0                                                                   #winCount-number of wins made by user
    lossCount=0                                                                  #lossCount- number of games lost by user
    userNumber=""                                                                #userNumber is given an initial value to start the loop.it will hold User Input.'X' is the sentinel of user input
    while userNumber!='X':
        loopTurn=0                                                               #loopTurn-counts the inner loop runs.It is incremented for every wrong match                
        gameCount+=1                                                             #Every new game will have new random number.When control enters outer loop,
        randNumber=random.randrange(1,13)                                        #consider as a new game
        while loopTurn<4:                             
            loopTurn+=1
            userNumber=input("Enter a number from 1 to 12. Enter X to exit:")
            if userNumber==str(randNumber):                                       #Converts the random number to string as input is in string
                print("Congratulation, correct! Let’s start a new secret number.")
                loopTurn=4                                                        #Set to 4 to exit loop and start new game."Instead of break statement"
                winCount+=1                                                       #Every correct match is a win,counter is incremented
            elif userNumber=='X':
                gameCount-=1                                                      #For every input X in between a game ,game wont be included,decrement counter
                loopTurn=4                                                        #"Instead of break statement".Set 4 to exit inner loop,userNumber =X it exits outer loop as well
            else:
                if loopTurn==4:                                                   # If trial reaches 4,game is lost.Counter incremented
                    print("Not correct. You have reached your fourth trial. The correct number is {0}.".format(randNumber))
                    print("Lets start a new secret number")
                    lossCount+=1       
                else:    
                    print("Not correct, try again:")
                
    if userNumber=='X':
        print("Here is your game summary:")
        print("Total games:{0:>26}".format(gameCount))
        print("Total game wins:{0:>22}".format(winCount))
        print("Total game losses:{0:>20}".format(lossCount))
        print()
        print("-----------------------------------------------")
main()    
