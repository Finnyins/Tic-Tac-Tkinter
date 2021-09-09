# Finn O'Brien
# Tic-Tac-Toe (Tkinter Edition)
# 8/18/2021

from tkinter import *


def clearscreen():
    menu.destroy()
    _list = mw.winfo_children()
    for item in _list:
        if item.winfo_children():
            item.pack_forget()

def display_board(board):  # function that displays the board
    g = len(board[0])
    for h in range(0, len(board)):
        print("+", end="")
        for l in range(0, g):
            print("---+", end="")
        print("")
        for l in range(0, g):
            print("| " + board[h][l] + " ", end="")
        print("|")
    print("+", end="")
    for l in board[0]:
        print("---+", end="")


# print("+---+---+---+")
# print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
# print("+---+---+---+")
# print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
# print("+---+---+---+")
# print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
# print("+---+---+---+")

def enter_move(board):  # function that registers the player's move and assigns it to the board.
    moved = 0
    while moved == 0:
        loop = 1
        while loop == 1:
            row = input("Please input the row of the tile you wish to claim: ")
            try:
                row = int(row) - 1
                if row > len(board) - 1:
                    print("That is not a valid row.")
                else:
                    loop = 0
            except ValueError:
                print("Please input a valid whole number.")
        loop = 1
        while loop == 1:
            move = input("Please input the number of the tile you wish to claim on the row: ")
            try:
                move = int(move)
                if move > len(board[0]) - 1:
                    print("That is not a valid tile.")
                else:
                    loop = 0
            except ValueError:
                print("Please input a valid whole number.")

        if board[row][move] == "X" or board[row][move] == "O":
            print("Slot already taken. please try a different slot")
        else:
            board[row][move] = "O"
            moved = 1
            return board


def freeslots(board):  # unused function. was intended to be used for the CPU player, but wasn't needed.
    slots = []
    free = []
    g = len(board[0])
    for h in range(0, len(board)):
        for l in range(0, g):
            if l != "X" or "O":
                free.append(l)
        slots.append(free)
        free = []
    return slots


def victory_for(board, a):  # win checker
    sign = ""
    win = False
    g = len(board[0])
    # checks for horizontal win
    for x in range(0, len(board)):
        if board[x][0] == a:
            if all(element == board[x][0] for element in board[x]):
                win = True
                sign = board[x][0]
                break
    # checks for vertical win
    for y in range(0, g):
        if board[0][y] == a:
            if all(element[y] == board[0][y] for element in board):
                win = True
                sign = board[0][y]
                break
    # checks for diagonal win
    if len(board[0]) == len(
            board):  # checks if board length and width are equal, as diagonals only work on square boards
        if board[0][0] == a:
            diag = []
            number = 0
            for x in range(0, len(board)):
                if board[number][number] == a:
                    diag.append(board[number][number])
                number += 1
            if len(diag) == len(board):
                win = True
                sign = board[0][0]
        if board[0][-1] == a:
            diag = []
            number = 0
            num2 = -1
            for x in range(0, len(board)):
                if board[number][num2] == a:
                    diag.append(board[number][num2])
                number += 1
                num2 -= 1
            if len(diag) == len(board):
                win = True
                sign = board[0][-1]

    if win == True:
        if sign == "X":
            print("Game Over. The computer wins.")
            return "end"

        elif sign == "O":
            print("Game Won. Congratulations!")
            return "end"

    else:
        numlist = []
        for h in range(0, len(board)):
            for z in board[h]:
                if z.isnumeric():
                    numlist.append(z)
        if len(numlist) == 0:
            print("Draw. Everyone loses.")
            return "end"

        else:
            return "cont"


def draw_move(board):  # Makes a random move for the CPU player
    from random import randrange
    freespace = freeslots(board)
    g = len(board[0])
    compmoved = 0
    while compmoved != 1:
        for x in range(1):
            comprow = randrange(0, len(board))
            compmove = randrange(0, g)
        if board[comprow][compmove] == "X" or board[comprow][compmove] == "O":
            compmoved = 0
        else:
            board[comprow][compmove] = "X"
            compmoved = 1

    return board


def playgame(
        board):  # function that runs the game, calling each of the methods when they are needed. The "skeleton" of the game.
    game = "continue"
    display_board(board)
    while game != "end":
        print("Computer's turn")
        board = draw_move(board)
        display_board(board)
        game = victory_for(board, "X")
        if game == "end":
            break
        print("Your Turn")
        board = enter_move(board)
        display_board(board)
        game = victory_for(board, "O")


def generateboard(l, h):  # function that is used to collect the user's input and generate a game board using it
    board = []
    boardlength = []
    for x in range(0, h):
        for x in range(0, l):
            boardlength.append(str(x))
        board.append(boardlength)
        boardlength = []
    return board


def generateboardvals():  # function that gathers the player's input to generate the board with.
    clearscreen()
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    for x in range(0, 3):
        menu.rowconfigure(x, weight=1)
        menu.columnconfigure(x, weight=1)
    header.pack(side="top", expand=False)
    menu.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    text = Label(header, text="Select Board Size", font=("Franklin Gothic", 25), bg="white", fg="snow4")
    text.pack(side="bottom", anchor="center", pady=(y / 5))


# main menu segment. Nothing particularly special here.
mw = Tk()
mw.config(bg="white")
mw.geometry("1280x720")
mw.minsize(1280, 720)
mw.title("Tic-Tac-Tkinter Version Pre-Alpha 0.1")
mw.update()
clearscreen()
loop = 1
played = 0
win1 = 0
win2 = 0
global x
global y
x = mw.winfo_screenwidth()
y = mw.winfo_screenheight()
header = Frame(mw, bg="lightsteelblue4", width=x, height=(y * 0.15))
menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
footer = Frame(mw, bg="grey40", width=x, height=(y * 0.15))
for x in range(0, 3):
    menu.rowconfigure(x, weight=1)
    menu.columnconfigure(x, weight=1)
header.pack(side="top", expand=False)
menu.pack(anchor="center", expand=True)
footer.pack(side="bottom", expand=False)
header.config(bg="white")
footer.config(bg="white")
menu.update()
titletext = Label(header, bg="white", fg="snow4", text="Tic-Tac-Tkinter", font=("Franklin Gothic", 25))
titletext.pack(side="bottom", anchor="center", pady=(y/5))
single = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Singleplayer")
multi = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Multiplayer")
options = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Options")
quit = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Quit Game")
single.grid(row=0, column=1, sticky=NS+W, pady=(y/100))
multi.grid(row=0, column=2, sticky=NS+E, pady=(y/100))
options.grid(row=1, column=1, sticky=NS+W, pady=(y/100))
quit.grid(row=1, column=2, sticky=NS+E, pady=(y/100))


mw.mainloop()



