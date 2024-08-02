import tkinter #Stands for tk-interface (graphical user interface library)

def set_tile(row, column): #function takes in a row and column number in reference to the board.
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
       #already taken spot
        return
    
    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switch player
        curr_player = playerX
    
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"

#check winner
    check_winner()


def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                #.config changes code
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
                game_over = True 


#vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
                game_over = True 

#diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
    and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_grey)
    

#anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
    and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_grey)
        board[1][1].config(foreground=color_yellow, background=color_light_grey)
        board[2][0].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return
    

#tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_grey)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX #Starting player
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]] #2D list

color_blue = "#4584b6" #Heximal representation of the color
color_yellow = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"

turns = 0
game_over = False


#window setup
window = tkinter.Tk() #create the game window
window.title("Tic-Tac-Toe")
window.resizable(False, False) #user cannot resize width or height of window

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_grey, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we") #columnspan will occupy 3 columnns.  sticky will stretch the label "we" (West to east) 
frame.pack()

#going to do a double for loop and assign each '0' in line 7-9 a 'button'
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), 
                                            background=color_grey, foreground=color_blue, width=4, height=1, #W & H in screen units, NOT pxls
                                            command=lambda row=row, column=column: set_tile(row, column)) # lambda function because we already know what the row and column numbers are for each button.
        board[row][column].grid(row=row+1, column=column) #row+1 because index starts at 0 but at row 0 we have the label. 

    button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_grey, foreground="white", command=new_game)

    button.grid(row=4, column=0, columnspan=3, sticky="we")

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop() #create a loop to keep the window open

