#File:racquet86448.py
#Author:Simmy PAyyappilly Varghese,StudentID:86448
#Date Created:04/03/2015
"""This program is a racquetball SImulation.

   It accepts the probability to win the game by A and B and number of games and print report on the wins of
   player A and player B.
"""

from random import *
def main():
    printIntro()
    probA,probB,numGames=getInputs()
    winsA,winsB=gameSimulator(numGames,probA,probB)
    prtSummary(winsA,winsB)

"""This function prints the Introduction.
  
   :Return -None
"""
def printIntro():
    print("This program simulates the racquet ball game between two players 'A' and 'B'")
    print("The abilities of each player is indicated by probability(a number between 0 & 1)that the player wins point by serving")
    print("PlayerA always has the first serve")
    print()

"""This function accepts input from the user.

    It accespts the probability of Player A to win the serve,Player B to win the serve and number
    of games to simulate
    :Return a-probability of Player A to win the serve
            b-probability of Player B to win the serve
            n-Number of games to Simulate
"""
def getInputs():
    a = eval(input("What is the probability player A wins a serve? "))
    b = eval(input("What is the probability player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n


"""This function simulate the racquet ball game.

    :param numGames-Number of games to Simulate
        probA-probability of Player A to win the serve
        probB-probability of Player B to win the serve
    :Return winsA-number of wins for A
            winsB-number of wins for B
"""
def gameSimulator(numGames,probA,probB):
    winsA=0
    winsB=0
    for i in range(numGames):
        scoreA,scoreB=simOneGame(probA,probB)
        if scoreA>scoreB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA,winsB


"""This function simulate the racquet ball game for one  game.

    :param probA-probability of Player A to win the serve
           probB-probability of Player B to win the serve
    :Return scoreA-score of Player A
            acoreB-score of Player B
"""
def simOneGame(probA,probB):
    scoreA=0
    scoreB=0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA=scoreA+1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB=scoreB+1
            else:
                serving="A"
    return scoreA,scoreB

            

"""This function Checks if any of the player won game.

    :param a-Score of Player A
           b-Score of Player B
    :Return True if any of the Score is 15 else False
"""        
def gameOver(a,b):
    if a==15 or b==15:
        return True
    else:
        return False


    
"""This function prints the summary of games.

    :param winsA-Games won by Player A
           winsB-Game won by  Player B
    :Return None
"""      
def prtSummary(winsA,winsB):
    n=winsA+winsB
    print("Games Simulated:",n)
    print("Wins for A {0} ({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B {0} ({1:0.1%})".format(winsB,winsB/n))

if __name__=='__main__':
    main() 




