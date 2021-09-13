# Finn O'Brien
# Tic-Tac-Toe (Tkinter Edition)
# 8/18/2021

from tkinter import *
from threading import *
import _thread



class start(Thread):
    def __init__(self, mw, header, footer, board, mode):
        self.mw = mw
        self.header = header
        self.footer = footer
        self.board = board
        self.mode = mode
        playgame(board, mode)


def clearscreen():
    _list = mw.winfo_children()
    for item in _list:
        if item.winfo_children():
            item.pack_forget()



# print("+---+---+---+")
# print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
# print("+---+---+---+")
# print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
# print("+---+---+---+")
# print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
# print("+---+---+---+")

def enter_move(board, num):  # function that registers the player's move and assigns it to the board.
    global contin
    global plr
    if plr == 1:
        board.buttons[num].config(text="O")
    if plr == 2:
        board.buttons[num].config(text="X")
    board.buttons[num]["state"] = "disabled"
    for button in board.buttons:
        button["state"] = "disabled"
    contin.set(True)


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


def playgame(board, mode):  # function that runs the game, calling each of the methods when they are needed. The "skeleton" of the game.
    board.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    footer.config(bg="grey40")
    footer.pack_propagate(False)
    footertext = Label(footer, font=("Franklin Gothic", 25), bg="grey40", fg="white")
    footertext.pack(anchor="center")
    footer.update()
    global plr
    global contin
    contin = BooleanVar()
    plr = 1
    game = "continue"
    while game != "end":
        if mode == "multi":
            plr = 1
            footertext.config(text="Player 1's Turn.")
            footertext.update()
            for x in board.buttons:
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False)
            board.wait_variable(contin)
            plr = 2
            footertext.config(text="Player 2's Turn.")
            footertext.update()
            for x in board.buttons:
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False)
            board.wait_variable(contin)
        else:
            footertext.config(text="Computer's Turn.")
            footertext.update()
            if game == "end":
                break
            contin.set(False)
            footertext.config(text="Your Turn")
            footertext.update()
            for x in board.buttons:
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"


def generateboard(s, mode):  # function that is used to collect the user's input and generate a game board using it
    global x
    global y
    global board
    clearscreen()
    board = Frame(mw, width=x, height=(y * 0.6))
    board.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    board.buttons = []
    for v in range(0, (s-1)):
        board.rowconfigure(v, weight=1)
        board.columnconfigure(v, weight=1)
    z = 0
    y = 0
    for m in range(0, s*s):
        board.buttons.append(Button(board, text=m+1, bg="ivory4", fg="white", font=("Franklin Gothic", 25), command=lambda m=m: enter_move(board, m), state="disabled"))
        board.buttons[m].grid(row=z, column=y, sticky=NSEW)
        board.buttons[m].update()
        y += 1
        if y == s:
            y = 0
            z += 1
    board = board
    _thread.start_new_thread(start, (mw, header, footer, board, mode))



def generateboardvals(mode):  # function that gathers the player's input to generate the board with.
    clearscreen()
    global menu
    menu.destroy()
    global x
    global y
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    for v in range(0, 4):
        menu.rowconfigure(v, weight=1)
        menu.columnconfigure(v, weight=1)
    header.pack(side="top", expand=False)
    menu.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    titletext.destroy()
    text = Label(header, text="Select Board Size", font=("Franklin Gothic", 25), bg="white", fg="snow4")
    text.pack(side="bottom", anchor="center", pady=(y / 5))
    size1 = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="3x3", command=lambda: generateboard(3, mode))
    size2 = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="5x5", command=lambda: generateboard(5, mode))
    size3 = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="7x7", command=lambda: generateboard(7, mode))
    size4 = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="9x9", command=lambda: generateboard(9, mode))
    size1.grid(row=0, column=1, sticky=NSEW, pady=(y / 100))
    size2.grid(row=0, column=2, sticky=NSEW, pady=(y / 100))
    size3.grid(row=1, column=1, sticky=NSEW, pady=(y / 100))
    size4.grid(row=1, column=2, sticky=NSEW, pady=(y / 100))


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
global menu
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
single = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Singleplayer", command=lambda: generateboardvals("single"))
multi = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Multiplayer", command=lambda: generateboardvals("multi"))
options = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Options")
quit = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Quit Game")
single.grid(row=0, column=1, sticky=NS+W, pady=(y/100))
multi.grid(row=0, column=2, sticky=NS+E, pady=(y/100))
options.grid(row=1, column=1, sticky=NS+W, pady=(y/100))
quit.grid(row=1, column=2, sticky=NS+E, pady=(y/100))


mw.mainloop()



