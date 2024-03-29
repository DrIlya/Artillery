import math
import module_ball as m_b


class Gun:
    """Класс, предназначенный для создания пушки"""
    def __init__(self, canvas, x=40, y=450, g=1, ball_live=150,  bullet=0):
        self.bullet = bullet
        self.balls = []

        self.x = x
        self.y = y
        self.g = g
        self.ball_live = ball_live

        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.canvas = canvas
        self.id = self.canvas.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.bullet += 1
        new_ball = m_b.Ball(self.canvas, self.x, self.y, self.g, self.ball_live)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
        self.canvas.coords(self.id, 20, 450,
                           20 + max(self.f2_power, 20) * math.cos(self.an),
                           450 + max(self.f2_power, 20) * math.sin(self.an)
                           )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.canvas.itemconfig(self.id, fill='orange')
        else:
            self.canvas.itemconfig(self.id, fill='black')
