import tkinter as tk
from tkinter import ttk
import sys


class GUI(object):
    def __init__(self, master, cmd):
        object.__init__(self)
        self.master = master
        self.cmd = cmd

        # Create elements
        self.frame = ttk.Frame(self.master)
        self.button = ttk.Button(self.frame, text='Test', command=self.cmd.button)

        # If you need to pass arguments to the function, use lambda
        # self.button = ttk.Button(self.frame, text='Test', command=lambda: self.cmd.nothing(5))

        # Pack elements
        self.frame.pack()
        self.button.pack()


class Commands(object):
    def __init__(self):
        object.__init__(self)

    @staticmethod
    def button():
        print('Button command')

    @staticmethod
    def nothing(number):
        print('What? Nothing! Or maybe {}!'.format(number))


def main():
    root = tk.Tk()

    gui = GUI(root, Commands())
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
