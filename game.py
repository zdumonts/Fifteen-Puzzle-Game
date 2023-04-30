# assignment: PA 5
# author: Zander Dumont-Strom
# date: 3/17/2023
# file: game.py
# program that used fifteen.py to create a GUI of the game where the user can press buttons to move the tiles

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          

def clickButton(event):
    # get the button that was clicked
    for i in range(16):
        if event.widget == buttons[i]:
            game.update(game.tiles[i])
            for j in range(16):
                # update the buttons
                buttons[j].configure(text = str(game.tiles[j]))
            break
    # check if the game is solved
    if game.is_solved():
        print("You won in {} moves!".format(game.moves))
        window.destroy()
    
if __name__ == '__main__':    
    window = Tk() # create the window
    window.title("Fifteen")
    window.configure(background = "black")
    myFont = font.Font(family='Helvetica', size=20, weight='bold')

    game = Fifteen() # create the game
    game.shuffle() # shuffle the game

    buttons = [] # create the buttons
    for i in range(16):
        buttons.append(Button(window, text = str(game.tiles[i]), font = myFont, height = 2, width = 4, bg = "white")) # create the button and add it to the list of buttons
        buttons[i].grid(row = i//4, column = i%4)
    
    
    shuffle = Button(window, text = "Sh", font = myFont, height = 2, width = 4, bg = "white", command = lambda: shuffle()) # shuffle button
    shuffle.grid(row = 4, column = 0)
    def shuffle(): # shuffle function
        game.shuffle()
        for i in range(16):
            buttons[i].config(text = str(game.tiles[i]))


    # bind the event handler to the buttons
    for i in range(16):
        buttons[i].bind("<Button-1>", clickButton)
    # start the game
    window.mainloop()
