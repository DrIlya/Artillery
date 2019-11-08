import time
import module_targets as m_t
import module_gun as m_g


class Basis:
    def __init__(self, place):
        self.place = place
        self.root = place.root
        self.canvas = place.canv

        self.t1 = m_t.Target(self.canvas)
        self.t2 = m_t.Target(self.canvas)
        self.targets = m_t.Targets(self.canvas, self.t1, self.t2)
        self.g1 = m_g.Gun(self.canvas)

        self.screen1 = self.canvas.create_text(400, 300, text='', font='28')

    def new_game(self, event=''):
        self.targets.renew()
        self.g1.balls = []
        self.canvas.bind('<Button-1>', self.g1.fire2_start)
        self.canvas.bind('<ButtonRelease-1>', self.g1.fire2_end)
        self.canvas.bind('<Motion>', self.g1.targetting)

        while self.targets.alive() or self.g1.balls:
            self.t1.move_t()
            self.t2.move_t()
            for b in self.g1.balls:
                if b.move():
                    self.g1.balls.remove(b)
                b.hittest(self.targets)
                if not self.targets.alive():
                    self.canvas.bind('<Button-1>', '')
                    self.canvas.bind('<ButtonRelease-1>', '')
                    self.canvas.itemconfig(self.screen1,
                                           text='Вы уничтожили все цели за ' + str(self.g1.bullet) + ' выстрелов')
            self.canvas.update()
            time.sleep(0.03)
            self.g1.targetting()
            self.g1.power_up()
        self.canvas.itemconfig(self.screen1, text='')
        self.root.after(750, self.New())

    def New(self):
        self.new_game()