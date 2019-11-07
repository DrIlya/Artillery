import time
import module_root as m_r
import module_targets as m_t
import module_gun as m_g


def new_game(event=''):
    global targets, screen1, t1, t2
    targets.renew()
    m_g.balls = []
    m_r.canv.bind('<Button-1>', g1.fire2_start)
    m_r.canv.bind('<ButtonRelease-1>', g1.fire2_end)
    m_r.canv.bind('<Motion>', g1.targetting)

    while targets.alive() or m_g.balls:
        t1.move_t()
        t2.move_t()
        for b in m_g.balls:
            if b.move():
                m_g.balls.remove(b)
            b.hittest(targets)
            if not targets.alive():
                m_r.canv.bind('<Button-1>', '')
                m_r.canv.bind('<ButtonRelease-1>', '')
                m_r.canv.itemconfig(screen1, text='Вы уничтожили все цели за ' + str(m_g.bullet) + ' выстрелов')
        m_r.canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    m_r.canv.itemconfig(screen1, text='')
    m_r.root.after(750, new_game)


t1 = m_t.Target()
t2 = m_t.Target()
targets = m_t.Targets(t1, t2)

screen1 = m_r.canv.create_text(400, 300, text='', font='28')
g1 = m_g.Gun()

new_game()

m_r.root_mainloop()