import tkinter as tk


class Place:
    def __init__(self, x_size, y_size):
        self.root = tk.Tk()
        self.fr = tk.Frame(self.root)
        self.size = str(x_size) + 'x' + str(y_size)
        self.root.geometry(self.size)
        self.canv = tk.Canvas(self.root, bg='white')
        self.canv.pack(fill=tk.BOTH, expand=1)


def root_mainloop():
    tk.mainloop()