import Game_basis
import module_root as m_r

# Создаем поле для игры, устанавливаем размеры и цвет поля
place_1 = m_r.Place(800, 600, canvas_color='white')

# Создаем основные объекты игры, устанавливаем цвет цели, коэффициент скорости цели, гравитацию и время жизни мяча
my_game = Game_basis.Basis(place_1, target_color='green', speed_factor=2, g=2, ball_live=200)

# Создаем игру
my_game.new_game()

m_r.root_mainloop()
