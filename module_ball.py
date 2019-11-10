from random import choice
import module_targets as m_t


class Ball:
    def __init__(self, canvas, x=40, y=450, g=1, ball_live=150):
        """ Конструктор класса ball(мяч)

        Args:
        canvas - графическое окно
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = g
        self.color = choice(['blue', 'green', 'yellow', 'brown'])
        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = ball_live

    def set_coords(self):
        """Метод устанавливает координаты мяча"""
        self.canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """
        self.live -= 1

        if self.x + self.r >= 790:
            self.vx = -0.6 * abs(self.vx)
            self.vy = 0.8 * self.vy
        elif self.x - self.r <= 10:
            self.vx = 0.6 * abs(self.vx)
            self.vy = 0.8 * self.vy
        self.x += self.vx

        if self.y + self.r >= 590:
            self.vy = 0.6 * abs(self.vy)
            self.vx = 0.8 * self.vx
        self.y -= self.vy
        self.vy -= self.g
        self.set_coords()

        if self.live <= 0:
            return self.delete()
        else:
            return False

    def hittest(self, obj):
        """Метод проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if isinstance(obj, m_t.Targets):
            points = 0
            for t in obj.t_list:
                if ((self.x - t.x) ** 2 + (self.y - t.y) ** 2 <= (self.r + t.r) ** 2) and t.live:
                    t.hit()
                    points += 1
            obj.hit(points)
            return points
        else:
            return False

    def delete(self):
        """Метод удаляет мяч с графического окна а также возвращает True, если это произошло"""
        self.canvas.delete(self.id)
        return True
