from tkinter import *
import random
from math import ceil
from time import sleep
from tkinter.messagebox import showinfo


class Board(Tk):
	def __init__(self, **lis):
		super().__init__()
		self.lis = lis
		self.geometry('500x600')
		self.resizable(0, 0)
		self.title('Ludo')

		self.canvas = Canvas(self, height=500, width=500, bg='white', borderwidth=-0)
		self.canvas.place(x=0, y=0)

		self.current_player = Label(self, text='RED', font='arial 18 bold')
		self.current_player.place(x=0, y=501)

		self.dice = Button(self, text='', bg=self.current_player.cget(
			'text').lower(), font='arial 30 bold', command=self.dice_number)
		self.dice.place(x=200, y=501, height=100, width=100)

		self.colors = ['red', 'blue', 'green', 'yellow']

		self.create_board()

		self.height = 450 / 15
		self.width = 450 / 15
		for key, values in lis.items():
			for i in values:
				self.canvas.create_rectangle(i[0], i[1], i[0] + (500 / 15), i[1] + (500 / 15), fill=key)
				self.player = Button(self, bg=key, relief=SUNKEN, activebackground='black', borderwidth=0, padx=0,
									 pady=0)
				self.player.place(x=i[0] + 25 / 15, y=i[1] + 25 / 15, height=self.height, width=self.width)
				self.player.bind('<Button-1>', self.on_dice)

		self.out = [[False for j in range(4)] for i in range(4)]
		self.moves = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.valid_moves = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.direction = [[[500 / 15, 0], [500 / 15, 0], [500 / 15, 0], [500 / 15, 0]],
						  [[0, 500 / 15], [0, 500 / 15], [0, 500 / 15], [0, 500 / 15]],
						  [[-500 / 15, 0], [-500 / 15, 0], [-500 / 15, 0], [-500 / 15, 0]],
						  [[0, -500 / 15], [0, -500 / 15], [0, -500 / 15], [0, -500 / 15]]]
		self.color = ['red', 'green', 'yellow', 'blue']
		self.win = [0, 0, 0, 0]

	def create_board(self):
		self.canvas.create_rectangle(
			(500 / 15), (500 / 15) * 7, (500 / 15) * 6, (500 / 15) * 8, fill='red')
		self.canvas.create_rectangle(
			(500 / 15) * 7, (500 / 15), (500 / 15) * 8, (500 / 15) * 7, fill='green')
		self.canvas.create_rectangle(
			(500 / 15) * 9, (500 / 15) * 7, (500 / 15) * 14, (500 / 15) * 8, fill='yellow')
		self.canvas.create_rectangle(
			(500 / 15) * 7, (500 / 15) * 9, (500 / 15) * 8, (500 / 15) * 14, fill='blue')
		for i in range(15):
			self.canvas.create_line(0, i * (500 / 15), 500, i * (500 / 15))

		for i in range(15):
			self.canvas.create_line(i * (500 / 15), 0, i * (500 / 15), 500)

		for i in range(2):
			for j in range(2):
				self.canvas.create_rectangle(i * (500 / 15) * 9, j * (500 / 15) * 9, i * (500 / 15) * 9 + 6 * (
						500 / 15), j * (500 / 15) * 9 + 6 * (500 / 15), fill=self.colors[i + i + j])
				self.canvas.create_rectangle(i * (500 / 15) * 9 + (500 / 15), j * (500 / 15) * 9 + (
						500 / 15), i * (500 / 15) * 9 + 5 * (500 / 15), j * (500 / 15) * 9 + 5 * (500 / 15),
											 fill='white')

		self.canvas.create_rectangle(
			500 / 15, (500 / 15) * 6, (500 / 15) * 2, (500 / 15) * 7, fill='red')
		self.canvas.create_rectangle(
			(500 / 15) * 8, (500 / 15), (500 / 15) * 9, (500 / 15) * 2, fill='green')
		self.canvas.create_rectangle(
			(500 / 15) * 6, (500 / 15) * 14, (500 / 15) * 7, (500 / 15) * 13, fill='blue')
		self.canvas.create_rectangle(
			(500 / 15) * 14, (500 / 15) * 8, (500 / 15) * 13, (500 / 15) * 9, fill='yellow')

		self.canvas.create_rectangle(
			(500 / 15) * 6, (500 / 15) * 6, (500 / 15) * 9, (500 / 15) * 9, fill='black')

		self.canvas.create_rectangle((500/15)*6,(500/15)*2,(500/15)*7,(500/15)*3, fill='gray72')
		self.canvas.create_rectangle((500/15)*12,(500/15)*6,(500/15)*13,(500/15)*7, fill='gray72')
		self.canvas.create_rectangle((500/15)*8,(500/15)*12,(500/15)*9,(500/15)*13, fill='gray72')
		self.canvas.create_rectangle((500/15)*2,(500/15)*8,(500/15)*3,(500/15)*9, fill='gray72')
	def dice_number(self):
		for i in range(10):
			x = random.randint(1, 6)
			self.dice.config(text=x)
			sleep(0.05)
			self.dice.update()
		if self.dice.cget('text') != 6 and True not in self.out[self.color.index(self.dice.cget('bg'))]:
			try:
				self.current_player.config(
					text=self.color[self.color.index(self.current_player.cget('text').lower()) + 1].upper())
			except IndexError:
				self.current_player.config(text='red')
			sleep(0.5)
			self.dice.config(bg=self.current_player.cget('text').lower())

			self.dice['state'] = NORMAL
			self.dice['text'] = 0
			for i in self.winfo_children():
				i['state'] = NORMAL

			return
		for w in self.winfo_children():
			if w.cget('bg') != self.dice.cget('bg'):
				w['state'] = DISABLED
		self.dice['state'] = DISABLED

	def on_dice(self, event):
		if self.dice.cget('text') == 0 or self.dice.cget('text') == '':
			return
		button = event.widget
		index = self.color.index(button.cget('bg'))
		try:
			string = str(button)[-2] + str(button)[-1]
			string = int(string) - 2
		except:
			string = str(button)[-1]
			string = int(string) - 2
		if button.cget('bg') != self.dice.cget('bg'):
			return NONE
		if self.dice.cget('bg') == button.cget('bg'):
			if not self.out[index][string % 4] and self.dice.cget('text') == 6:
				if button.cget('bg') == 'red':
					button.place_configure(x=(500 / 15) + 25 / 15, y=((500 / 15) * 6) + 25 / 15)
				if button.cget('bg') == 'green':
					button.place_configure(x=((500 / 15) * 8) + 25 / 15, y=(500 / 15) + (25 / 15))
				if button.cget('bg') == 'blue':
					button.place_configure(x=((500 / 15) * 6) + 25 / 15, y=((500 / 15) * 13) + (25 / 15))
				if button.cget('bg') == 'yellow':
					button.place_configure(x=((500 / 15) * 13) + 25 / 15, y=((500 / 15) * 8) + (25 / 15))
				self.out[index][string % 4] = True

			else:
				if not self.out[index][string % 4]:
					if True in self.out[index]:
						return NONE
				if self.out[index][string % 4]:
					self.valid_moves[index][string % 4] += self.dice.cget('text')
					if self.valid_moves[index][string % 4] > 56:
						self.valid_moves[index][string % 4] -= self.dice.cget('text')
						return
					else:
						self.move(button, index, string)
				if self.dice.cget('text') == 6:
					self.dice['state'] = NORMAL
					self.dice['text'] = 0
					for i in self.winfo_children():
						i['state'] = NORMAL
					return
				try:
					self.current_player.config(
						text=self.color[self.color.index(self.current_player.cget('text').lower()) + 1].upper())
				except IndexError:
					self.current_player.config(text='RED')
				self.dice.config(bg=self.current_player.cget('text').lower())

		self.dice['state'] = NORMAL
		self.dice['text'] = 0
		for i in self.winfo_children():
			i['state'] = NORMAL

	def move(self, button, index, string):
		for i in range(self.dice.cget('text')):
			self.moves[index][string % 4] += 1
			pos = button.place_info()
			button.place_configure(x=float(pos.get('x')) + self.direction[index][string % 4][0],
								   y=float(pos.get('y')) + self.direction[index][string % 4][1])
			sleep(0.1)
			button.update()

			if self.moves[index][string % 4] in [5, 18, 31, 44]:
				if abs(self.direction[index][string % 4][0]) > abs(self.direction[index][string % 4][1]):
					button.update()
					if self.direction[index][string % 4][0] > 0:
						button.place_configure(y=float(pos.get('y')) - 500 / 15)
					else:
						button.place_configure(y=float(pos.get('y')) + 500 / 15)

				if abs(self.direction[index][string % 4][0]) < abs(self.direction[index][string % 4][1]):
					if self.direction[index][string % 4][1] > 0:
						button.place_configure(x=float(pos.get('x')) + 500 / 15)
					else:
						button.place_configure(x=float(pos.get('x')) - 500 / 15)
				self.direction[index][string % 4][0], self.direction[index][string % 4][1] = \
					self.direction[index][string % 4][1], -self.direction[index][string % 4][0]

			if self.moves[index][string % 4] in [10, 12, 23, 25, 36, 38, 49]:
				self.direction[index][string % 4][0], self.direction[index][string % 4][1] = -self.direction[index][
					string % 4][1], self.direction[index][string % 4][0]
			if self.moves[index][string % 4] == 50:
				self.direction[index][string % 4][0], self.direction[index][string % 4][1] = -self.direction[index][
					string % 4][1], self.direction[index][string % 4][0]
			if self.moves[index][string % 4] == 56:
				self.win[self.color.index(button.cget('bg'))] = self.win[self.color.index(button.cget('bg'))] + 1
				if 4 in self.win:
					showinfo('Winner', f'The Winner is {button.cget("bg")}')
					self.color.pop(self.win[self.color.index(button.cget('bg'))])

		self.collision(button)

	def collision(self, button):
		pos = button.place_info()
		if not self.validatin(pos):
			return
		x = int(pos.get('x'))
		y = int(pos.get('y'))
		collisions = 0
		child = [i for i in self.winfo_children()]
		for i in child:
			if 'button' in str(i):
				pos_ = i.place_info()
				x_ = int(pos_.get('x'))
				y_ = int(pos_.get('y'))
				for w in range(x, x + 30):
					for j in range(y, y + 30):
						if w in range(x_, x_ + 30) and j in range(y_, y_ + 30) and button.cget('bg') != i.cget('bg'):
							collisions += 1
			if collisions > 700:
				self.out_pawn(i, button)
				collisions = 0

	def validatin(self, pos):
		validation = 0
		for i in range(int(pos.get('x'))):
			for j in range(int(pos.get('y'))):
				if ceil((500 / 15) * 2) > i > ceil(500 / 15):
					if ceil((500 / 15) * 7) > j > ceil(500 / 15 * 6):
						validation += 1
				if ceil((500 / 15) * 8) < i < ceil((500 / 15) * 9):
					if ceil((500 / 15)) < j < ceil(500 / 15 * 2):
						validation += 1
				if ceil((500 / 15) * 6) < i < ceil((500 / 15) * 7):
					if ceil((500 / 15) * 13) < j < ceil((500 / 15) * 14):
						validation += 1
				if ceil((500 / 15) * 13) < i < ceil((500 / 15) * 14):
					if ceil((500 / 15) * 8) < j < ceil((500 / 15) * 9):
						validation += 1

				if ceil((500 / 15) * 7) > i > ceil((500 / 15) * 6):
					if ceil((500 / 15) * 3) > j > ceil((500 / 15) * 2):
						validation += 1
				if ceil((500 / 15) * 13) > i > ceil((500 / 15) * 12):
					if ceil((500 / 15) * 7) > j > ceil(500 / 15 * 6):
						validation += 1
				if ceil((500 / 15) * 9) > i > ceil((500 / 15) * 8):
					if ceil((500 / 15) * 13) > j > ceil((500 / 15) * 12):
						validation += 1
				if ceil((500 / 15) * 3) > i > ceil((500 / 15) * 2):
					if ceil((500 / 15) * 9) > j > ceil((500 / 15) * 8):
						validation += 1

		if validation > 700:
			return False
	def out_pawn(self, i, button):
		if i.cget('bg') != button.cget('bg'):
			index = self.color.index(i.cget('bg'))
			try:
				string = str(i)[-2] + str(i)[-1]
				string = int(string) - 2
			except:
				string = str(i)[-1]
				string = int(string) - 2
			print(self.lis.get(i.cget('bg'))[string % 4][0])
			print(self.lis.get(i.cget('bg'))[string % 4][1])
			i.place_configure(x=self.lis.get(i.cget('bg'))[string % 4][0] + (25 / 15),
							  y=self.lis.get(i.cget('bg'))[string % 4][1] + (25 / 15))
			self.moves[index][string % 4] = 0
			self.valid_moves[index][string % 4] = 0
			self.out[index][string % 4] = False
			if i.cget('bg') == 'red':
				self.direction[index][string % 4] = [500 / 15, 0]
			if i.cget('bg') == 'green':
				self.direction[index][string % 4] = [0, 500 / 15]
			if i.cget('bg') == 'yellow':
				self.direction[index][string % 4] = [-500 / 15, 0]
			if i.cget('bg') == 'blue':
				self.direction[index][string % 4] = [0, -500 / 15]
			i.update()


if __name__ == "__main__":
	player = Board(**{
		'red': [[500 / 15, 500 / 15], [500 / 15 * 4, 500 / 15], [500 / 15 * 4, 500 / 15 * 4], [500 / 15, 500 / 15 * 4]],
		'green': [[(500 / 15) * 10, (500 / 15)], [(500 / 15) * 13, (500 / 15)], [(500 / 15) * 13, (500 / 15) * 4],
				  [(500 / 15) * 10, (500 / 15) * 4]],
		"yellow": [[(500 / 15) * 10, (500 / 15) * 10], [(500 / 15) * 13, (500 / 15) * 10],
				   [(500 / 15) * 13, (500 / 15) * 13], [(500 / 15) * 10, (500 / 15) * 13], ],
		'blue': [[(500 / 15), (500 / 15) * 10], [(500 / 15) * 4, (500 / 15) * 10], [(500 / 15) * 4, (500 / 15) * 13],
				 [(500 / 15), (500 / 15) * 13]], })
	player.mainloop()
