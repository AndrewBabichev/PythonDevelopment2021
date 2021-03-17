import tkinter as tk
import numpy as np


class InputLabel(tk.Label):
    def remove_pointer(self, event = None):
        self.canvas.place(x = -1000, y = 0)
        self.frame_text.configure(relief = 'flat')
        self.frame_space.focus_set()

    def set_pointer(self, event):
        self.symbol_pointer = event.x // self.symbol_width
        self.canvas.place(x = self.symbol_pointer * self.symbol_width, y = 0)
        self.frame_text.configure(relief = 'ridge')
        self.focus_set()

    def restore_pointer(self, event):
        self.symbol_pointer = self.length
        self.canvas.place(x = self.symbol_pointer * self.symbol_width, y = 0)
        self.frame_text.configure(relief = 'ridge')
        self.focus_set()

    def key(self, event):
        if event.keysym == 'BackSpace':
            if (self.symbol_pointer > 0):
                self.text = self.text[:self.symbol_pointer - 1] + self.text[self.symbol_pointer:]
                self.symbol_pointer -= 1
                self.length -= 1
                self.config(text = self.text)

        elif event.keysym == 'Delete' or event.keysym == 'KP_Delete':
            if (self.symbol_pointer < self.length):
                self.text = self.text[:self.symbol_pointer] + self.text[self.symbol_pointer + 1:]
                self.length -= 1
                self.config(text = self.text)

        elif event.keysym == 'Left':
            self.symbol_pointer = max(0, self.symbol_pointer - 1)
        elif event.keysym == 'Right':
            self.symbol_pointer = min(self.length, self.symbol_pointer + 1)
        elif event.keysym == 'Home' or event.keysym == 'KP_Home':
            self.symbol_pointer = 0
        elif event.keysym == 'End' or event.keysym == 'KP_End':
            self.symbol_pointer = self.length
        elif event.keysym == 'Tab' or event.keysym == 'Return' or event.keysym == 'KP_Enter':
            pass
        elif event.keysym == 'Escape':
            self.remove_pointer()
            return

        elif (len(event.char) == 1):
            symbol = event.char
            self.text = self.text[:self.symbol_pointer] + symbol + self.text[self.symbol_pointer:]
            self.symbol_pointer += 1
            self.length += 1
            self.config(text = self.text)

        self.canvas.place(x = self.symbol_pointer * self.symbol_width, y = 0)
        size = max(58, (self.length + 2) * self.symbol_width + 2)
        self.frame_text.configure(width = size)
        self.frame_space.configure(width = size - 58 + 3)


    def __init__(self):
        self.text = ""
        self.length = 0
        self.symbol_pointer = 0
        self.symbol_width = 8

        self.frame_text = tk.Frame(bg = 'gray', bd = 4, width = 58, height = 35)
        self.frame_text.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.frame_optional = tk.Frame()
        self.frame_optional.grid(row = 1, column = 0)

        self.frame_space = tk.Frame(self.frame_optional, bg = 'gray', width = 3, height = 30)
        self.frame_button = tk.Frame(self.frame_optional, bg = 'gray')
        self.frame_space.grid(row = 0, column = 0)
        self.frame_button.grid(row = 0, column = 1)

        self.button = tk.Button(self.frame_button, text = 'Quit', bg = 'gray', command = self.quit)
        self.button.pack(side = tk.RIGHT)

        super().__init__(bg = 'gray', bd = 0, font = 'TkFixedFont', text = self.text)
        self.place(x = 8, y = 8)

        self.bind('<Button-1>', self.set_pointer)
        self.bind('<Key>', self.key)
        self.frame_space.bind('<Button-1>', self.remove_pointer)
        self.frame_text.bind('<Button-1>', self.restore_pointer)

        self.canvas = tk.Canvas(self, bg = 'black', bd = 0, width = 1, height = 20)


if __name__ == '__main__':
    app = InputLabel()
    app.mainloop()
