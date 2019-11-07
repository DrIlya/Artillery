from random import choice
import module_root as m_r
import module_targets as m_t


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'yellow', 'brown'])
        self.id = m_r.canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 150

    def set_coords(self):
        m_r.canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self, g=1):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
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
        self.vy -= g
        self.set_coords()

        if self.live <= 0:
            return self.delete()
        else:
            return False

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

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
        m_r.canv.delete(self.id)
        return True