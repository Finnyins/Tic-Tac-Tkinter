# Finn O'Brien
# Tic-Tac-Toe (Tkinter Edition)
# 8/18/2021

from tkinter import *
from threading import *
from tkinter import messagebox
import time


def placeholder():
    sign = ""
    win = False
    g = len(main[0])
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
    from random import choice
    compmoved = 0
    free = []
    for x in board.buttons:
        if x["text"] != "X" and x["text"] != "O":
            free.append(x)
    while compmoved != 1:
        move = choice(free)
        move["text"] = "X"
        compmoved = 1
    return board


def quit(event):
    quitbox = messagebox.askquestion("Exit", "Are you sure you would like to exit?", icon="warning")
    if quitbox == "yes":
        exit()
    else:
        return


class start(Thread):
    def __init__(self, mw, header, footer, board, mode):
        self.mw = mw
        self.header = header
        self.footer = footer
        self.board = board
        self.mode = mode
        playgame(board, mode)

class wait(Thread):
    def __init__(self, tm):
        self.tm = tm
        pause(tm)

def pause(tm):
    time.sleep(tm)

def clearscreen():
    _list = mw.winfo_children()
    for item in _list:
        for child in item.winfo_children():
            child.forget()
        if item.winfo_children():
            item.pack_forget()

def playagain(mode):
    clearscreen()
    header = Frame(mw, bg="lightsteelblue4", width=x, height=(y * 0.15))
    header.pack(side="top", expand=False)
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    for v in range(0, 4):
        menu.rowconfigure(v, weight=1)
        menu.columnconfigure(v, weight=1)
    menu.pack(anchor="center", expand=True)
    text = Label(header, bg="white", fg="ivory4", text="Would you like to play again?", font=("Franklin Gothic", 25))
    text.pack(anchor="center")
    yes = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Again", command=lambda: generateboardvals(mode))
    no = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="No", command=lambda: main())
    yes.grid(row=0, column=1, sticky=NSEW)
    no.grid(row=0, column=2, sticky=NSEW)




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


def victory_for(board, a, mode):  # win checker
    import math
    f = len(board.buttons)
    e = math.sqrt(f)
    i = 0
    sub = []
    main = []
    for x in range(0, (f)):
        sub.append(board.buttons[x]["text"])
        if len(sub) == e:
            main.append(sub)
            sub = []
        i += 1
    sign = ""
    win = False
    g = len(main[0])
    # checks for horizontal win
    for x in range(0, len(main)):
        if main[x][0] == a:
            if all(element == main[x][0] for element in main[x]):
                win = True
                sign = main[x][0]
                break
    # checks for vertical win
    for y in range(0, g):
        if main[0][y] == a:
            if all(element[y] == main[0][y] for element in main):
                win = True
                sign = main[0][y]
                break
    # checks for diagonal win
    if len(main[0]) == len(main):  # checks if board length and width are equal, as diagonals only work on square boards
        if main[0][0] == a:
            diag = []
            number = 0
            for x in range(0, len(main)):
                if main[number][number] == a:
                    diag.append(main[number][number])
                number += 1
            if len(diag) == len(main):
                win = True
                sign = main[0][0]
        if main[0][-1] == a:
            diag = []
            number = 0
            num2 = -1
            for x in range(0, len(main)):
                if main[number][num2] == a:
                    diag.append(main[number][num2])
                number += 1
                num2 -= 1
            if len(diag) == len(main):
                win = True
                sign = main[0][-1]

    if win == True:
        if sign == "X":
            if mode == "multi":
                footertext.config(text="Game Over. Player 2 Wins.")
            else:
                footertext.config(text="Game Over. The Computer Wins.")
        elif sign == "O":
            if mode == "multi":
                footertext.config(text="Game Over. Player 1 Wins.")
            else:
                footertext.config(text="Game Won. Congratulations!")
        mw.update()
        time.sleep(5)
        return "end"

    else:
        numlist = []
        for x in board.buttons:
            if x["text"] != "X" and x["text"] != "O":
                numlist.append(x["text"])
        if len(numlist) == 0:
            footertext.config(text="Draw. Everyone loses.")
            mw.update()
            time.sleep(5)
            return "end"
        else:
            return "cont"



def playgame(board, mode):  # function that runs the game, calling each of the methods when they are needed. The "skeleton" of the game.
    board.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    footer.config(bg="grey40")
    footer.pack_propagate(False)
    global footertext
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
            game = victory_for(board, "O", mode)
            if game == "end":
                break
            plr = 2
            footertext.config(text="Player 2's Turn.")
            footertext.update()
            for x in board.buttons:
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False)
            board.wait_variable(contin)
            game = victory_for(board, "X", mode)
            if game == "end":
                break
        else:
            footertext.config(text="Computer's Turn.")
            footertext.update()
            time.sleep(2)
            draw_move(board)
            game = victory_for(board, "X", mode)
            if game == "end":
                break
            contin.set(False)
            footertext.config(text="Your Turn")
            footertext.update()
            for x in board.buttons:
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False)
            board.wait_variable(contin)
            game = victory_for(board, "O", mode)
            if game == "end":
                break



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
        board.buttons.append(Button(board, text=str(m+1), bg="ivory4", fg="white", font=("Franklin Gothic", 25), command=lambda m=m: enter_move(board, m), state="disabled"))
        board.buttons[m].grid(row=z, column=y, sticky=NSEW)
        board.buttons[m].update()
        y += 1
        if y == s:
            y = 0
            z += 1
    board = board
    t = Thread(target=start(mw, header, footer, board, mode))
    t.start()
    t.join()
    playagain(mode)


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

def full(event):
    global fl
    if fl == False:
        mw.attributes("-fullscreen", True)
        fl = True
    elif fl == True:
        mw.attributes("-fullscreen", False)
        fl = False

def main():
    # main menu segment. Nothing particularly special here.
    clearscreen()
    loop = 1
    played = 0
    win1 = 0
    win2 = 0
    global x
    global y
    global fl
    x = mw.winfo_screenwidth()
    y = mw.winfo_screenheight()
    global header
    header = Frame(mw, bg="lightsteelblue4", width=x, height=(y * 0.15))
    global menu
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    global footer
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
    global titletext
    titletext = Label(header, bg="white", fg="snow4", text="Tic-Tac-Tkinter", font=("Franklin Gothic", 25))
    titletext.pack(side="bottom", anchor="center", pady=(y/5))
    single = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Singleplayer", command=lambda: generateboardvals("single"))
    multi = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Multiplayer", command=lambda: generateboardvals("multi"))
    options = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Options")
    quitbutton = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Quit Game", command=lambda: quit(0))
    single.grid(row=0, column=1, sticky=NS+W, pady=(y/100))
    multi.grid(row=0, column=2, sticky=NS+E, pady=(y/100))
    options.grid(row=1, column=1, sticky=NS+W, pady=(y/100))
    quitbutton.grid(row=1, column=2, sticky=NS+E, pady=(y/100))
    mw.bind("<Escape>", quit)
    mw.bind("<F11>", full)


    mw.mainloop()

if __name__ == "__main__":
    global mw
    mw = Tk()
    mw.config(bg="white")
    mw.geometry("1280x720")
    mw.minsize(1280, 720)
    mw.title("Tic-Tac-Tkinter Version Pre-Alpha 0.1")
    mw.update()
    main()

