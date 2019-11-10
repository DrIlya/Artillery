from random import randrange as rnd


class Target:
    def __init__(self, canvas, target_color='red', speed_factor=2):
        self.x = 0
        self.y = 0
        self.r = 0
        self.canvas = canvas

        self.color = target_color
        self.speed_F = speed_factor

        self.live = 1

        self.id = self.canvas.create_oval(0, 0, 0, 0)

        self.new_target()

        self.vx = 0
        self.vy = 0

    def new_target(self):
        """ Инициализация новой цели."""
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.vx = rnd(-3, 3) * self.speed_F
        self.vy = rnd(-3, 3) * self.speed_F
        self.live = 1
        self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.canvas.itemconfig(self.id, fill=self.color)

    def hit(self):
        """Попадание шарика в цель."""
        self.canvas.coords(self.id, -10, -10, -10, -10)
        self.live = 0

    def move_t(self):
        """Движение цели."""
        if self.live:
            if 200 <= self.x <= 750:
                pass
            elif self.x >= 750:
                self.vx = -abs(self.vx)
            elif self.x <= 200:
                self.vx = abs(self.vx)

            if 50 <= self.y <= 550:
                pass
            elif self.y >= 550:
                self.vy = -abs(self.vy)
            elif self.y <= 50:
                self.vy = abs(self.vy)

            self.x += self.vx
            self.y += self.vy

            self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        else:
            self.canvas.coords(self.id, -10, -10, -10, -10)


class Targets:
    def __init__(self, canvas, *args):
        self.t_list = list(args)
        self.points = 0
        self.canvas = canvas
        self.id_points = self.canvas.create_text(30, 30, text=self.points,
                                                 font='28')

    def add(self, *args):
        self.t_list.append(*args)
        return True

    def alive(self):
        flag = False
        for t in self.t_list:
            if t.live:
                flag = True
        return flag

    def hit(self, points=1):
        self.points += points
        self.canvas.itemconfig(self.id_points, text=self.points)

    def renew(self):
        for t in self.t_list:
            t.new_target()
