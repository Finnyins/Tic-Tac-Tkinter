# Finn O'Brien
# Tic-Tac-Toe (Tkinter Edition)
# 8/18/2021

from tkinter import *
from tkinter import messagebox
from threading import *
import time



def draw_move(board):  # Makes a random move for the CPU player
    from random import choice # imports random choice function
    compmoved = 0 # variable to determine whether CPU has moved or not
    free = [] # creating list that will contain all empty slots on the board
    for x in board.buttons: # gathering all slots that haven't been claimed and adding them to the "free" list
        if x["text"] != "X" and x["text"] != "O":
            free.append(x)
    while compmoved != 1:
        move = choice(free) # picking a random entry from the list of free slots
        move["text"] = "X" # claiming the randomly chosen free tile
        compmoved = 1
    return board # returning the updated board with the CPU's chosen move to the main game function


def quit(event):
    quitbox = messagebox.askquestion("Exit", "Are you sure you would like to exit?", icon="warning")
    if quitbox == "yes":
        mw.destroy()
        exit()
    else:
        return



def clearscreen(): # basic clearscreen function
    _list = mw.winfo_children()
    for item in _list:
        for child in item.winfo_children():
            child.pack_forget()
        if item.winfo_children():
            item.pack_forget()

def playagain(mode): # function to ask if the player wants to play again. no particularly special code in here
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
    global contin # initializes the global plr and contin variables
    global plr
    if plr == 1: # claims the chosen button with an "O" if it's player 1's turn
        board.buttons[num].config(text="O")
    if plr == 2: # claims the chosen button with an "X" if it's player 2's turn
        board.buttons[num].config(text="X")
    board.buttons[num]["state"] = "disabled" # disables the chosen button
    for button in board.buttons: # disables all buttons on the board so the player cannot pick more than one
        button["state"] = "disabled"
    contin.set(True) # sets the contin variable to true, indicating to the "playgame" function that the current player
                     # has taken their turn


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
    for x in range(0, len(main)):
        if main[x][0] == a:
            if all(element == main[x][0] for element in main[x]):
                win = True
                sign = main[x][0]
                break
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
    clearscreen()
    board.pack(anchor="center", expand=True) # placing the board and all other menu items on screen.
    footer.pack(side="bottom", expand=False)
    footer.config(bg="grey40")
    footer.pack_propagate(False)
    global footertext
    footertext = Label(footer, font=("Franklin Gothic", 25), bg="grey40", fg="white")
    footertext.pack(anchor="center")
    footer.update()
    global plr # making plr and contin global is necessary for use in multiple functions
    global contin
    contin = BooleanVar() # setting a variable for later use to determine when a player's turn has ended
    plr = 1 # setting the current player, to tell the game which sign should be used for the next move
    game = "continue" # setting the loop variable
    while game != "end": # setting the loop
        if mode == "multi": # code that runs only if multiplayer is enabled
            plr = 1 # setting the player to 1 again because it's running inside of the loop
            footertext.config(text="Player 1's Turn.")
            footertext.update()
            for x in board.buttons: # reactivating all buttons on the board that haven't already been claimed by X or O
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal" # reactivates buttons
            contin.set(False) # sets contin variable to false
            board.wait_variable(contin) # waits until the continue variable is changed by the "enter_move" function
            game = victory_for(board, "O", mode) # calls victory function to check whether the player using "O" has won
            if game == "end": # terminates the loop if the victory function sets the game variable to "end",
                break         # signifying that a player has won
            plr = 2 # sets player variable to 2, indicating that the second player is taking their turn
            footertext.config(text="Player 2's Turn.")
            footertext.update()
            for x in board.buttons: # reactivating all unclaimed buttons
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False) # setting the contin variable to false again
            board.wait_variable(contin) # waiting until "enter_move" function is called again and sets contin to true
            game = victory_for(board, "X", mode) # sets the game variable to the value returned by victory function
            if game == "end": # ends loop if victory function returns "end"
                break
        else: # this code runs if the game mode is set to singleplayer
            # CPU uses X's and Player uses O's btw
            footertext.config(text="Computer's Turn.")
            footertext.update()
            time.sleep(2) # simple wait command
            draw_move(board) # runs the function to generate the CPU's move on an empty tile
            game = victory_for(board, "X", mode) # checks to see if the player using X's (the CPU) has won
            if game == "end": # ends the game if the CPU has won
                break
            contin.set(False) # sets contin variable to False again
            footertext.config(text="Your Turn")
            footertext.update()
            for x in board.buttons: # reactivates any buttons that don't have an X or O already on them
                if x["text"] != "X" and x["text"] != "O":
                    x["state"] = "normal"
            contin.set(False) # sets contin variable to false again for some reason. this line of code is unnecessary
            board.wait_variable(contin) # waits until the contin variable is set back to true after the player moves
            game = victory_for(board, "O", mode) # checks if player won
            if game == "end": # terminates loop if player wins, if not the program goes back to the beginning of the
                              # [while game != "end":] loop
                break



def generateboard(s, mode):  # function that is used to collect the user's input and generate a game board using it
    global x
    global y
    global board
    clearscreen()
    board = Frame(mw, width=x, height=(y * 0.6), name="board")
    mw.nametowidget(".board")
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
    t = Thread(target=playgame(board, mode))
    t.start()
    t.join()
    playagain(mode)


def generateboardvals(mode):  # function that gathers the player's input to generate the board with.
    clearscreen()
    global x
    global y
    header.pack(side="top", expand=False)
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    menu.pack(anchor="center", expand=True)
    footer.pack(side="bottom", expand=False)
    for k in range(0, 3):
        menu.rowconfigure(k, weight=1)
        menu.columnconfigure(k, weight=1)
    header.config(bg="white")
    footer.config(bg="white")
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

def options():
    clearscreen()
    mw.update()
    global fl
    global footer
    footer.destroy()
    x = mw.winfo_screenwidth()
    y = mw.winfo_screenheight()
    header = Frame(mw, bg="white", width=x, height=(y * 0.15))
    header.pack(side="top", expand=False)
    menu2 = Frame(mw, bg="white", width=x, height=(y * 0.6))
    for v in range(0, 3):
        menu2.rowconfigure(v, weight=1)
        menu2.columnconfigure(v, weight=1)
    menu2.pack(anchor="center", expand=True)
    titletext = Label(header, bg="white", fg="snow4", text="Options", font=("Franklin Gothic", 25))
    titletext.pack(side="bottom", anchor="center", pady=(y / 5))
    titletext.config(text="Options")
    fll = Button(menu2, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Toggle Fullscreen", command=lambda:full(0))
    bck = Button(menu2, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Back", command=main)
    fll.grid(row=0, column=2)
    bck.grid(row=1, column=2)

def main():
    # main menu segment. Nothing particularly special here.
    clearscreen()
    global fl
    fl = False
    global x
    global y
    x = mw.winfo_screenwidth()
    y = mw.winfo_screenheight()
    mw.config(bg="white")
    global header
    header = Frame(mw, bg="lightsteelblue4", width=x, height=(y * 0.15))
    global menu
    menu = Frame(mw, bg="white", width=x, height=(y * 0.6))
    global footer
    footer = Frame(mw, bg="grey40", width=x, height=(y * 0.15))
    for k in range(0, 3):
        menu.rowconfigure(k, weight=1)
        menu.columnconfigure(k, weight=1)
    header.pack(side="top", expand=False)
    menu.pack(anchor="center", expand=False)
    footer.pack(side="bottom", expand=False)
    header.config(bg="white")
    footer.config(bg="white")
    global titletext
    titletext = Label(header, bg="white", fg="snow4", text="Tic-Tac-Tkinter", font=("Franklin Gothic", 25))
    titletext.pack(side="bottom", anchor="center", pady=(y/5))
    single = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Singleplayer", command=lambda: generateboardvals("single"))
    multi = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Play Multiplayer", command=lambda: generateboardvals("multi"))
    option = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Options", command=options)
    quitbutton = Button(menu, bg="ivory4", fg="white", font=("Franklin Gothic", 25), text="Quit Game", command=lambda: quit(0))
    single.grid(row=0, column=1, sticky=NS+W)
    multi.grid(row=0, column=2, sticky=NS+E)
    option.grid(row=1, column=1, sticky=NS+W)
    quitbutton.grid(row=1, column=2, sticky=NS+E)
    mw.update()
    menu.update()
    mw.bind("<Escape>", quit)
    mw.bind("<F11>", full)


    mw.mainloop()

if __name__ == "__main__":
    mw = Tk()
    mw.geometry("1280x720")
    mw.minsize(1280, 720)
    mw.title("Tic-Tac-Tkinter Version 1.1")
    mw.update()
    main()
