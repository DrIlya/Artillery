import tkinter as tk


class Place:
    """Класс, создающий поле для игры (root и canvas).
    Конструктор принимает размеры геометрии окна: x_size и y_size
    и цвет окна (белый по умолчанию) """
    def __init__(self, x_size, y_size, canvas_color='white'):
        self.root = tk.Tk()
        self.fr = tk.Frame(self.root)
        self.size = str(x_size) + 'x' + str(y_size)
        self.root.geometry(self.size)

        self.color = canvas_color
        self.canv = tk.Canvas(self.root, bg=self.color)
        self.canv.pack(fill=tk.BOTH, expand=1)


def root_mainloop():
    """Запускает главный цикл обработки событий"""
    tk.mainloop()