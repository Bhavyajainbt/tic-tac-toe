# This is our tic tac toe game.
print("This is Tic Tac Toe game designed by Bhavya Tongya!!!!")

import random

# board list

board = [0,1,2,
         3,4,5,
         6,7,8]

# board view

def show():
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])

# check board line

def checkline(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

#check board

def checkall(char):
    if checkline(char,0,1,2):
        return True
    if checkline(char,3,4,5):
        return True
    if checkline(char,6,7,8):
        return True
    if checkline(char,0,3,6):
        return True
    if checkline(char,1,4,7):
        return True
    if checkline(char,2,5,8):
        return True
    if checkline(char,0,4,8):
        return True
    if checkline(char,2,4,6):
        return True

# our main game loop

while True:
       inp = int(input("Select the spot:"))
       if board[inp] != "x" and board[inp] != "o":
           board[inp] = "x"

           if checkall("x") == True:
              print("Player wins!")
              break


           while True:
              opponent = random.randint(0,8)

              if board[opponent] != "x" and board[opponent] != "o":
                 board[opponent] = "o"

                 if checkall("o") == True:
                   print("Computer wins!")
                   break

                 break
       else:
           print("The spot has already been taken!")

       show()

