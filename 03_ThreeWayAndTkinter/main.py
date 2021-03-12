import tkinter as tk
from tkinter import messagebox
from functools import partial
import numpy as np

board_shape = (4, 4)

class Application:
    def __init__(self):
        self.i, self.j = board_shape[0] - 1, board_shape[1] - 1 # empty space location
        self.board_buttons = np.zeros(board_shape, dtype = tk.Button)
        self.board_numbers = np.arange(1, 17).reshape(4, 4)

    def shuffle(self):
        pass

    def check_victory(self):
        if (np.array_equal(self.board_numbers, np.arange(1, 17).reshape(4, 4))):
            messagebox.showinfo(message = "Victory")
            self.shuffle()

    def move(self, i, j):
        if (np.abs(self.i - i) + np.abs(self.j - j) == 1):
            self.board_buttons[i, j].grid_forget()
            self.board_buttons[self.i, self.j].configure(text = str(self.board_numbers[i, j]))
            self.board_buttons[self.i, self.j].grid(row = self.i, column = self.j, sticky = tk.NSEW)

            self.board_numbers[self.i, self.j], self.board_numbers[i, j] = self.board_numbers[i, j], self.board_numbers[self.i, self.j]
            self.i, self.j = i, j

            self.check_victory()

    def create_board(self, root):
        root.rowconfigure(0, weight = 0)
        root.rowconfigure(1, weight = 1)
        root.columnconfigure(0, weight = 1)

        self.menu = tk.Frame(root)
        self.menu.columnconfigure(0, weight = 1, minsize = 75)
        self.menu.columnconfigure(1, weight = 1, minsize = 75)
        self.menu.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.new = tk.Button(self.menu, text = "New", command = self.shuffle)
        self.new.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.exit = tk.Button(self.menu, text = "End", command = root.quit)
        self.exit.grid(row = 0, column = 1, sticky = tk.NSEW)

        self.board = tk.Frame(root)
        self.board.grid(row = 1, column = 0, sticky = tk.NSEW)
        for i in range(board_shape[0]):
            self.board.rowconfigure(i, weight = 1, minsize = 75)
            for j in range(board_shape[1]):
                self.board.columnconfigure(j, weight = 1, minsize = 75)
                self.board_buttons[i, j] = tk.Button(self.board, text = str(self.board_numbers[i, j]), command = partial(self.move, i, j))
                self.board_buttons[i, j].grid(row = i, column = j, sticky = tk.NSEW)

        self.board_buttons[self.i, self.j].grid_forget()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tag game')

    Game = Application()
    Game.create_board(root)

    root.mainloop()
