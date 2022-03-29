"""
Created on 12/19/21

@author: aoshotse
"""

import turtle
"""
       Notes for what to do:
       - Program in a PvP and PvCPU mode, and prompt user to pick at
           the beginning
       - maybe try to use a nested function to choose between PvP and CPU mode?
       """
win_dict = {}
x_xlist = []
x_ylist = []
x_alr = []
o_xlist = []
o_ylist = []
o_alr = []
x_win = set()
o_win = set()
draw = False
playerX = 0
playerO = 0
tie = 0
no_overlap = []

""""All the glboal variables are listed above. win_dict is a log of the shape and its corresponding locations on the grid. 
    x_xlist and x_ylist are lists of the x and y coordinates for the X. o_xlist and o_ylist are lists of the x and y 
    coordinates of the O. x_alr and o_alr are lists that of coordinates for the X and Os so that the x and y coordinates are 
    not added to x_xlist, x_ylist, o_xlist, and o_ylist more than once.x_win is is a set that tells when X wins. o_win 
    is a set that tells when O wins. playerX is the win count for X and playerO is the win count for O. tie is the count 
    for the number of ties. no_overlap is a list of all the is used to store all the positions of the Xs and Os so that 
    they can be no overlapping."""


def change(x,y):
    """This fucntion switches between X and O with a mouse-click.
        This was designed to assist in switching between Players after a turn."""
    player.hideturtle()
    if player.shape() == "x.gif":
        player.shape("circle")
        player.goto(x,y)
    else:
        player.shape("x.gif")
        player.goto(x,y)
def win_conditions():
    """this function tracks the positioning of each X and O in order to declare a winner
        given the event of a win"""
    global x_xlist
    global x_ylist
    global x_alr
    global x_win
    global o_xlist
    global o_ylist
    global o_alr
    global o_win
    global draw
    for (shape,list) in win_dict.items():
        if shape == 'x.gif':
            for (x,y) in list:
                if (x,y) not in x_alr:
                    x_xlist.append(x)
                    x_ylist.append(y)
                    x_alr.append((x,y))
            for elem in x_xlist:
                if x_xlist.count(elem) == 3:
                    x_win.add(True)
                else:
                    x_win.add(False)
            for elem in x_ylist:
                if x_ylist.count(elem) == 3:
                    x_win.add(True)
                else:
                    x_win.add(False)
            if (-136.50,135.00) in x_alr and (1.50,-3.00) in x_alr and (139.50,-140.00) in x_alr:
                x_win.add(True)
            if (139.50,135.00) in x_alr and (1.50,-3.00) in x_alr and (-136.50,-140.00) in x_alr:
                x_win.add(True)
        else:
            for (x,y) in list:
                if (x,y) not in o_alr:
                    o_xlist.append(x)
                    o_ylist.append(y)
                    o_alr.append((x,y))
            for elem in o_xlist:
                if o_xlist.count(elem) == 3:
                    o_win.add(True)
                else:
                    o_win.add(False)
            for elem in o_ylist:
                if o_ylist.count(elem) == 3:
                    o_win.add(True)
                else:
                    o_win.add(False)
            if (-136.50,135.00) in o_alr and (1.50,-3.00) in o_alr and (139.50,-140.00) in o_alr:
                o_win.add(True)
            if (139.50,135.00) in o_alr and (1.50,-3.00) in o_alr and (-136.50,-140.00) in o_alr:
                o_win.add(True)
        if len(x_alr + o_alr) == 9:
            draw = True
def match_done():
    """this function returns 'X' if Player 1 wins or 'O' if Player 2 wins."""
    if True in x_win:
        return 'X'
    if True in o_win:
        return 'O'
    if draw == True:
        return "Tie"
def pos_directory():
    """this function keeps track of every positon of each X and O on the grid"""
    global win_dict
    if player.shape() not in win_dict:
        win_dict[player.shape()] = []
    win_dict[player.shape()].append(player.pos())
def player_mvmnt(x,y):
    """this function controls the placement of each X and O on the grid (placement is by mouse click)."""
    global no_overlap
    player.penup()
    player.speed(0)
    player.setpos(x,y)
    if player.xcor() >= -200 and player.xcor() <= 203 and player.ycor() >= -202 and player.ycor() <= 198:
        if player.ycor() > 72:
            if player.xcor() < -73:
               player.goto(-136.5, 135)
            elif player.xcor() > -73 and player.xcor() < 76:
                player.goto(1.5,135)
            else:
                player.goto(139.5,135)
        if player.ycor() > -78 and player.ycor() < 72:
            if player.xcor() < -73:
                player.goto(-136.5,-3)
            elif player.xcor() > -73 and player.xcor() < 76:
                player.goto(1.5,-3)
            else:
                player.goto(139.5,-3)
        if player.ycor() < -78:
            if player.xcor() < -73:
                player.goto(-136.5,-140)
            elif player.xcor() > -73 and player.xcor() < 76:
                player.goto(1.5,-140)
            else:
                player.goto(139.5,-140)
        if player.pos() not in no_overlap:
            player.stamp()
            no_overlap.append(player.pos())
            pos_directory()
            change(0, 0)
        else:
            player.home()
    else:
        player.home()
    win_conditions()
def game_over():
    """this function closes the window after the user no longer
        wishes to continue"""
    wn.bye()
def game_engine(x,y):
    """this function runs and manages the game and declares a winner."""
    global playerX
    global playerO
    global tie
    global x_xlist
    global x_ylist
    global x_alr
    global x_win
    global o_xlist
    global o_ylist
    global o_alr
    global o_win
    global draw
    player_mvmnt(x,y)
    game = match_done()
    if game == 'X':
        wn.title("Winner!!!")
        clear_score = Blockout(-130,-275)
        playerX += 1
        new_score = Words(-140, -300, "arrow", "white", str(playerX), "left", ("courier new", 40, "bold"))
        text = wn.textinput("Player 1 wins!", "Continue? 'y' or 'n'")
    if game == 'O':
        wn.title("Winner!!!")
        clear_score = Blockout(140, -275)
        playerO += 1
        new_score = Words(132, -300, "arrow", "white", str(playerO), "left", ("courier new", 40, "bold"))
        text = wn.textinput("Player 2 wins!", "Continue? 'y' or 'n'")
    if game == 'Tie':
        wn.title("Tie!!!")
        clear_score = Blockout(-10, -275)
        tie += 1
        new_score = Words(-10, -300, "arrow", "white", str(tie), "left", ("courier new", 40, "bold"))
        text = wn.textinput("Tie!", "Continue? 'y' or 'n'")
    if text == "y":
        wn.title("Tic-Tac-Toe")
        player.clearstamps()
        win_dict.clear()
        x_xlist.clear()
        x_ylist.clear()
        x_alr.clear()
        o_xlist.clear()
        o_ylist.clear()
        o_alr.clear()
        x_win.clear()
        o_win.clear()
        no_overlap.clear()
        draw = False
        player.shape('x.gif')
    else:
        wn.title("Ending Game....")
        wn.clearscreen()
        wn.screensize(400, 300, "black")
        end_game = Words(1.5,-3, "arrow", "white","Game Over", "center", ("courier new", 60, "bold"))
        wn.ontimer(game_over,2000)

if __name__ == '__main__':
    # Screen setup + register shape
    wn = turtle.Screen()
    wn.title("Tic-Tac-Toe")
    wn.screensize(400, 300, "black")
    wn.register_shape("x.gif")

    # drawing grid
    """Used a class in order to draw the grid with the color white. Same color 
        was used to draw the bound."""
    class Bound(turtle.Turtle):
        """This class draws the boundary for the game. The bound for the game is
            650x600"""
        def __init__(self, x, y, turn, xmove, ymove):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.speed(0)
            self.color("white")
            self.penup()
            self.setpos(x, y)
            self.pendown()
            for x in range(2):
                self.forward(xmove)
                self.left(turn)
                self.forward(ymove)
                self.left(turn)
    class Grid(turtle.Turtle):
        """This class draws the 3x3 grid for the Tic-Tac-Toe game"""
        def __init__(self, x, y, turn, move):
            turtle.Turtle.__init__(self)
            self.speed(10)
            self.color("black")
            self.hideturtle()
            self.color("white")
            self.right(turn)
            self.penup()
            self.setpos(x, y)
            self.pendown()
            self.forward(move)
    bound = Bound(-325, -300, 90, 650, 600)
    grid1 = Grid(-200, -75, 0, 400)
    grid2 = Grid(-200, 75, 0, 400)
    grid3 = Grid(-75, 200, 90, 400)
    grid4 = Grid(75, 200, 90, 400)

    # On-Screen Text
    class Words(turtle.Turtle):
        """This class is used for writing the all the words/phrases
            that will be appearing on the screen"""
        def __init__(self, x, y, shape, color, phrase, align, font):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.shape(shape)
            self.color(color)
            self.speed(0)
            self.penup()
            self.goto(x,y)
            self.write(phrase, align=align, font=font)
    title = Words(0,225,"arrow","white","Tic-Tac-Toe",'center',("courier new", 40, "bold"))
    score_design = Words(10,-250,"arrow","white", "Player 1 Wins:     Ties:     Player 2 Wins: ","center",("courier new", 16, "bold"))
    score_numX = Words(-140, -300, "arrow","white", str(playerX), "left", ("courier new", 40, "bold"))
    score_numO = Words(137, -300, "arrow","white", str(playerO), "left", ("courier new", 40, "bold"))
    score_tie = Words(-10, -300, "arrow","white", str(tie), "left", ("courier new", 40, "bold"))

    class Blockout(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.speed(0)
            self.penup()
            self.shape("square")
            self.shapesize(2)
            self.goto(x,y)
            self.stamp()

    # Creating Player + Player details
    """Called the class 'Player' in order to design both
        player 1 and player 2."""
    class Player(turtle.Turtle):
        """This class designs the player's color, shape, and size"""
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.color("blue")
            self.shape("x.gif")
            self.shapesize(5)
    player = Player()

    wn.listen()
    wn.onscreenclick(game_engine)
    wn.mainloop()