import Game_basis
import module_root as m_r


place_1 = m_r.Place(800, 600)
my_game = Game_basis.Basis(place_1)
my_game.new_game()
m_r.root_mainloop()