# Holds all board values
theBoard = {7: " ", 8: " ", 9: " ",
            4: " ", 5: " ", 6: " ",
            1: " ", 2: " ", 3: " "}

# Vars
count = 0  # Check for draw
x = 0  # No of X wins
o = 0  # No of O wins

# At start
print("Welcome to Tic Tac Toe")


# Printing the board function with values
def printBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# X move
def x_move():
    global count  # accessing count var
    printBoard(theBoard)
    move = int(input("It is X turn. Move to which place (1-9): "))
    if theBoard[move] == " " and 0 < move < 10:  # if spot is emtpy and the move is between 1-9
        count += 1  # count goes up by 1

        theBoard[move] = "X"  # Set that position to X

        checkBoard()
        o_move()
    elif theBoard[move] != " ":  # Already filled
        print("Place is already filled pick another place. Pick another!")
        x_move()  # Repeat
    elif move <= 0 or move > 9:  # Number not within 1-9
        print("Please select a number between 1 and 9!")
        x_move()
    else:  # If player enters something other than a number
        print("Please enter a correct input!!")
        x_move()


# O move
def o_move():
    global count  # getting var count
    printBoard(theBoard)
    move = int(input("It is O turn. Move to which place (1-9): "))
    if theBoard[move] == " " and 0 < move <= 9:  # if spot is emtpy and the move is between 1-9
        count += 1  # Count goes up by 1

        theBoard[move] = "O"  # Set the position to O

        checkBoard()
        x_move()
    elif theBoard[move] != " ":  # Already filled
        print("Place is already filled pick another place. Pick another!")
        o_move()
    elif move <= 0 or move > 9:  # Not within range
        print("Please select a number between 1 and 9!")
        o_move()
    else:  # not a number
        print("Please enter a correct input!!")
        o_move()


# Checking for a win
def checkBoard():
    global count, x, o  # accessing all these vars

    # All the following if and elif statements check for a winning move
    if theBoard[7] == theBoard[8] == theBoard[9] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[4] == theBoard[5] == theBoard[6] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[1] == theBoard[2] == theBoard[3] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[1] == theBoard[4] == theBoard[7] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[2] == theBoard[5] == theBoard[8] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[3] == theBoard[6] == theBoard[9] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[1] == theBoard[5] == theBoard[9] == "X":

        repeatFuncX()
    elif theBoard[3] == theBoard[5] == theBoard[7] == "X":
        x += 1
        repeatFuncX()
    elif theBoard[7] == theBoard[8] == theBoard[9] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[4] == theBoard[5] == theBoard[6] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[1] == theBoard[2] == theBoard[3] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[1] == theBoard[4] == theBoard[7] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[2] == theBoard[5] == theBoard[8] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[3] == theBoard[6] == theBoard[9] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[1] == theBoard[5] == theBoard[9] == "O":
        o += 1
        repeatFuncO()
    elif theBoard[3] == theBoard[5] == theBoard[7] == "O":
        o += 1
        repeatFuncO()

    # When count is 9 means a draw cause the board is filled
    if count == 9:
        printBoard(theBoard)
        clearBoard()
        print("Draw!!")
        replay()
        count = 0


# Simplifies code instead of repetition
def repeatFuncX():
    printBoard(theBoard)
    printStatementX()
    x_move()


# Simplifies code instead of repetition
def repeatFuncO():
    printBoard(theBoard)
    printStatementY()
    x_move()


# Printing win statements for X
def printStatementX():
    print("X won!!")
    print("End Game")
    replay()


# Printing win statements for O
def printStatementY():
    print("O won!!")
    print("End Game")
    replay()


# Clearing the board
def clearBoard():
    global count  # Accessing count
    count = 0  # Set count to 0 to restart

    # while loop to simplify code
    i = 1
    while i < 10:  # While i is less than 10
        theBoard[i] = " "  # Set the value of i of board to " " which means emtpy
        i += 1  # i plus 1
    # Repeats 9 times


# Replaying game
def replay():
    replayStr = str(input("Would you like to replay the game? (y/n): "))  # Getting input as a string
    if replayStr == "y" or replayStr == "Y":  # If input is Y or y
        checkScore()
        clearBoard()
        x_move()
    elif replayStr == "n" or replayStr == "N":  # If input is N or n
        print("Goodbye!!")
        quit()  # Ends programme without errors
    else:
        # If input is not Y or N
        print("Please enter the correct input!!")
        replay()


# Printing scores
def checkScore():
    global x, o  # Accessing vars
    print("Score")
    print("X: ", x)
    print("O: ", o)


# Continuous loop
while True:
    # For start
    if count == 0:
        x_move()

    # Checking for a draw
    if count == 9:
        clearBoard()
        print("Draw!!")
        replay()
        count = 0
