"""

Author: Nefi Aguilar 
Description:
 The program will use Python Turtle Graphics to display a maze.
 Then the prigram will use the drowing of the maze to play a videogame
 that will prompt the user for choises. Each choise will advance the
 turtle pointer through the maze.
  
"""
from turtle import *

def playEscapeTheMazeGame():
    printInstructions()
    if (isReadyToPlay()):
        drawMaze()
        hasTheKey = False
        firstChoise(hasTheKey)
    

def printInstructions():
    print('Welcome to the maze runner game!')
    print('In order to win this game you will have to find the hidden key ', end=' ')
    print('to open the exit door.')
    print('Your survival will depend on your intuition.')
    
    
def isReadyToPlay():
    print('Are you ready to play? (yes/no) ', end="")
    if (getYesNoAnswer()):
        return True
    else:
        print('Alright, come back when you are ready!')
        return False
    
def getYesNoAnswer():
    answer = input("")
    while not(answer == 'yes' or answer == 'Yes' or answer == 'no'
              or answer == 'No'):
        answer = input('Please answer with a "yes" or "no" ')
    if (answer == 'yes' or answer == 'Yes'):
        return True
    else:
        return False    

def makeAPause():
    pause = input('Press enter to continue: ')
       
def drawMaze():
    #frame
    speed(100)
    penup()
    goto(-200, -50)
    pendown()
    right(90)
    forward(150)
    left(90)
    forward(400)
    left(90)
    forward(250)
    right(90)
    forward(20)
    right(90)
    forward(100)
    right(90)
    forward(20)
    right(90)
    forward(100)
    pendown()
    forward(150)
    left(90)
    forward(400)
    left(90)
    forward(150)
    penup()
    #first Block
    goto(-150, 150)
    pendown()
    forward(300)
    left(90)
    forward(100)
    left(90)
    forward(300)
    left(90)
    forward(100)
    penup()
    #second Block
    goto(200, 50)
    pendown()
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(150)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(50)
    penup()
    #thirth Block
    goto(200, -50)
    pendown()
    forward(250)
    right(180)
    forward(50)
    right(90)
    forward(100)
    left(90)
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(100)
    penup()
    #baul 1
    goto(125, -122.5)
    pendown()
    circle(5)
    penup()
    #baul 2
    goto(75, 80)
    pendown()
    circle(5)
    penup()
    #finish
    goto(-200, 0)
    right(180)
    speed(3)
    
def promptForChoise():
    choise = input("Go right or left (r/l) ")
    while (choise != "r" and choise != "l"):
        print("Invalid answer")
        print('Type "r" for Right or "l" for Left"')
        choise = input("Go right or left (r/l) ")
    return choise
       
def firstChoise(hasTheKey):
    choise = promptForChoise()
    if (choise == "r"):
        firstChoiseR(hasTheKey)
    else:
        firstChoiseL(hasTheKey)
    
def firstChoiseR(hasTheKey):
    forward(25)
    right(90)
    forward(175)
    left(90)
    forward(150)
    left(45)
    secondChoiseR = promptForChoise()
    if (secondChoiseR == "r"):
        secondChoiseRR(hasTheKey)
    else:
        secondChoiseRL()
   
def secondChoiseRR(hasTheKey):
    right(45)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(100)
    if (hasTheKey):
        print("looks like you have already been here...")
        makeAPause()
    else:
        print("Congratulations! You found the key to open the exit door")
        hasTheKey = True
        makeAPause()
    print("Lets take you back to the begining so that you can find ", end="")
    print("the exit door")
    makeAPause()
    left(180)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(150)
    right(90)
    forward(100)
    right(90)
    forward(350)
    right(90)
    forward(175)
    left(90)
    forward(25)
    left(180)
    firstChoise(hasTheKey)
    
def secondChoiseRL():
    left(45)
    forward(100)
    print("You got lost!   'n' ")
    gameOver()
               
def firstChoiseL(hasTheKey):
    forward(25)
    left(90)
    forward(175)
    right(90)
    forward(150)
    right(45)
    choise = promptForChoise()
    if (choise == "l"):
        secondChoiseLL()
    else:
        secondChoiseLR(hasTheKey)
    
def secondChoiseLL():
    left(45)
    forward(200)
    right(90)
    forward(100)
    right(180)
    print("You got lost!   'n' ")
    gameOver()
    
def secondChoiseLR(hasTheKey):
    right(45)
    forward(175)
    left(90)
    forward(200)
    if (hasTheKey):
        print("Fantastic! You have the key to open the exit door")
        useKey = input("Press enter to use the key: ")
        forward(300)
        wonGame()
    else:
        print("Looks like you have found the exit door, but you need ", end="")
        print("a key to open it.")
        makeAPause()
        left(180)
        forward(50)
        right(45)
        print("You can go right or go back to the begining of the maze ", end="")
        print("to look for the key.")
        print("Do you want to go right (yes/no) ", end="")
        if (getYesNoAnswer()):
            thirdChoiseLRR()
        else:
            print("Alright! Lets get you back to the begining.")
            makeAPause()
            left(45)
            forward(150)
            right(90)
            forward(175)
            left(90)
            forward(150)
            left(90)
            forward(175)
            right(90)
            forward(25)
            right(180)
            firstChoise(hasTheKey)

def thirdChoiseLRR():
    right(45)
    forward(125)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    print("It was a trap! 'n' ")
    gameOver()
    
def gameOver():
    left(45)
    forward(15)
    pendown()
    right(180)
    forward(30)
    penup()
    left(135)
    forward(21.2132)
    pendown()
    left(135)
    forward(30)
    left(135)
    penup()
    tryGameAgain()
    
def tryGameAgain():
    print("Do you want to try this game again? (yes/no) ", end="")
    if (getYesNoAnswer()):
        print("Alright !")
        goto(-200, 0)
        hasTheKey = False
        firstChoise(hasTheKey)
        
    else:
        print("Alright ! See you soon.")
         
def wonGame():
    print("*" * 50)
    print("*{:^48}*".format(""))
    print("*{:^48}*".format("You won the game!"))
    print("*{:^48}*".format(""))
    print("*" * 50)
       
    
playEscapeTheMazeGame()

    
    
