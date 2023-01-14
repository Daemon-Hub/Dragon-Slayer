from tkinter import Tk, Canvas, Frame, PhotoImage
from random import randint

# Окно
window = Tk()

w = 600
h = 600

window.geometry("{}x{}".format(w,h))
window.wm_iconbitmap("icon.ico")
window.title("Dragon Slayer")

# Холст
canvas = Canvas(window, width=w, height=h)
canvas.pack()

frame = Frame(window, borderwidth = 10)
frame.pack()

# Фон
bg_photo = PhotoImage(file='bg_2.png')

#Класс рыцарь
class Knight:

	def __init__(self):
		# Скорость рыцаря
		self.v_x = 0
		self.v_y = 0
		# Координаты рыцаря
		self.x = 70
		self.y = h//2
		# Изображение рыцаря
		self.photo = PhotoImage(file='knight.png')

	def up(self, event):
		self.v_y = -3

	def down(self, event):
		self.v_y = 3

	def right(self, event):
		self.v_x = 3

	def left(self, event):
		self.v_x = -3

	def stop(self, event):
		self.v_x = 0
		self.v_y = 0


knight = Knight()

# Класс дракон
class Dragon:

	def __init__(self):
		# Скорость рыцаря
		self.v = randint(1, 3)
		# Координаты рыцаря
		self.x = w + 50
		self.y = randint(100, h - 100)
		# Изображение рыцаря
		self.photo = PhotoImage(file='dragon.png')


# Создание драконов
dragons = []

for i in range(randint(1, 7)):
	dragons.append(Dragon())

# Процесс игры
def game():

	# Пересоздание холста с фоном
	canvas.delete('all')
	canvas.create_image(w // 2, h // 2, image=bg_photo)
	canvas.create_image(knight.x, knight.y, image=knight.photo)

	# Движение рыцаря

	# Право | Лево
	if knight.x < 50:
		knight.x = 50
	elif knight.x > 550:
		knight.x = 550
	else:
		knight.x += knight.v_x

	# Верх | Вниз
	if knight.y < 50:
		knight.y = 50
	elif knight.y > 550:
		knight.y = 550
	else:
		knight.y += knight.v_y

	# Статус дракона
	current_dragon = 0
	dragon_to_kill = -1

    # Столкновение с дроконом
	for dragon in dragons:
		dragon.x -= dragon.v
		canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

		# Столкновение
		if ((dragon.x-knight.x)**2) + ((dragon.y-knight.y)**2) <= (96)**2:
			dragon_to_kill = current_dragon

		current_dragon += 1

		# Проигрыш
		if dragon.x <= 0:
			canvas.delete('all')
			canvas.create_text(w//2, h//2, text='You LOSS!!!', font='Verdana 42', fill='red')
			break

	# Убийство дракона
	if dragon_to_kill >= 0:
		del dragons[dragon_to_kill]

	# Выгрыш
	if len(dragons)==0:
		canvas.delete('all')
		canvas.create_text(w//2, h//2, text='You WIN!!!', font='Verdana 42', fill='green')

	# Продолжаем игру
	else:
		window.after(30, game)

# Кнопки
window.bind('w', knight.up)
window.bind('s', knight.down)
window.bind('a', knight.left)
window.bind('d', knight.right)
window.bind('<KeyRelease>', knight.stop)

# Запустить игру
game()

# Работа окна
window.mainloop()