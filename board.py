import random
import time

class Board:

	# Board
	def __init__(self):
		self.row_1 = [0, 0, 0, 0]
		self.row_2 = [0, 0, 0, 0]
		self.row_3 = [0, 0, 0, 0]
		self.row_4 = [0, 0, 0, 0]

		self.grid = [self.row_1,
					 self.row_2,
					 self.row_3,
					 self.row_4]

	# Display Board
	def display(self):

		self.r = 0
		self.cells = []

		print(' -------------------')
		for row in self.grid:
			self.r += 1
			print('|',end='')
			for cell in row:
				if cell >= 1000:
					print('' + str(cell), end='|')
				elif cell >= 100:
					print(' ' + str(cell), end='|')	
				elif cell >= 10:
					print(' ' + str(cell), end=' |')	
				elif cell == 0:
					print('   ', end=' |')
				else:
					print('  ' + str(cell), end=' |')			

			print()
			if self.r <= 3: print('|----+----+----+----|')
			else: print(" -------------------")

	# Update board
	def update(self):

		self.cells = []
		self.row_count = 0
		self.cell_count = 0 
		self.value = random.choice((2, 4))

		# get all empty cells
		for row in self.grid:
			self.row_count += 1
			self.cell_count = 0
			for cell in row:
				self.cell_count += 1
				if cell == 0:
					self.cells.append((self.row_count-1, self.cell_count-1))

		# put a value in a random empty cell
		if self.cells:
			self.rand_cell = random.choice(self.cells)
			self.grid[self.rand_cell[0]][self.rand_cell[1]] = self.value

	# Score
	def score(self, game):
		
		self.game = game
		self.cells = []

		for row in self.grid:
			for cell in row:
				self.cells.append(cell)

		if self.game:
			print("\nYour score: " + str(sum(self.cells))+".\n")
		else:
			print("\nYour score was: " + str(sum(self.cells))+".\n")

	# Check if there are any possible moves left
	def check(self):
	
		self.r = 0
		self.c = 0
		self.moves = 0

		for row in self.grid:
			for cell in self.grid[self.r]:
				try:
					# cell is 0
					if cell == 0:
						self.moves += 1
					# check up
					if self.r != 3:
						if self.grid[self.r][self.c] == self.grid[self.r+1][self.c]:
							self.moves += 1
					# check down
					if self.r != 0:
						if self.grid[self.r][self.c] == self.grid[self.r-1][self.c]:
							self.moves += 1
					# check left
					if self.c != 0:
						if self.grid[self.r][self.c] == self.grid[self.r][self.c-1]:
							self.moves += 1
					# check right
					if self.c != 3:
						if self.grid[self.r][self.c] == self.grid[self.r][self.c+1]:
							self.moves += 1
				except:
					pass

				self.c += 1
			self.r += 1
			self.c = 0 	

		return self.moves		

	# Movement in a direction
	def move(self, direction):
		self.direction = direction
		
		for i in range(1, 4):
			if direction == 'up':
				self.r = 3
				self.c = 0
			elif direction == 'down':
				self.r = 0
				self.c = 0
			elif direction == 'left':
				self.r = 0
				self.c = 3
			elif direction == 'right':
				self.r = 0
				self.c = 0

			for row in self.grid:
				for cell in self.grid[self.r]:

					if direction == 'up':
						if self.r == 0:
							break
						if self.grid[self.r-1][self.c] == 0:
							self.grid[self.r-1][self.c] = self.grid[self.r][self.c]
							self.grid[self.r][self.c] = 0
						self.c += 1

					elif direction == 'down':
						if self.r == 3:
							break
						if self.grid[self.r+1][self.c] == 0:
							self.grid[self.r+1][self.c] = self.grid[self.r][self.c]
							self.grid[self.r][self.c] = 0
						self.c += 1

					elif direction == 'left':
						if self.r == 4:
							break
						if self.c > 0:
							if self.grid[self.r][self.c-1] == 0:
								self.grid[self.r][self.c-1] = self.grid[self.r][self.c]
								self.grid[self.r][self.c] = 0
						self.c -= 1

					elif direction == 'right':
						if self.r == 4:
							break
						if self.c < 3:
							if self.grid[self.r][self.c+1] == 0:
								self.grid[self.r][self.c+1] = self.grid[self.r][self.c]
								self.grid[self.r][self.c] = 0
						self.c += 1

				if direction == 'up': 
					self.r -= 1 
					self.c = 0
				elif direction == 'down':
					self.r += 1
					self.c = 0
				elif direction == 'left':
					self.r += 1
					self.c = 3
				elif direction == 'right':
					self.r += 1
					self.c = 0

	# Merge in a direction
	def merge(self, direction):
		self.direction = direction

		if direction == 'up':
			self.r = 0
			self.c = 0
		elif direction == 'down':
			self.r = 3
			self.c = 0
		elif direction == 'left':
			self.r = 0
			self.c = 0
		elif direction == 'right':
			self.r = 0
			self.c = 3

		for row in self.grid:
			for cell in self.grid[self.r]:
				
				if direction == 'up':
					if self.r == 3:
						break
					if self.grid[self.r+1][self.c] == self.grid[self.r][self.c]:
						self.grid[self.r+1][self.c] = self.grid[self.r+1][self.c] * 2
						self.grid[self.r][self.c] = 0
					self.c += 1

				elif direction == 'down':
					if self.r == 0:
						break
					if self.grid[self.r-1][self.c] == self.grid[self.r][self.c]:
						self.grid[self.r][self.c] = self.grid[self.r][self.c] * 2
						self.grid[self.r-1][self.c] = 0 
					self.c += 1

				elif direction == 'left':
					if self.r == 4:
						break
					if self.c >= 1:
						if self.grid[self.r][self.c-1] == self.grid[self.r][self.c]:
							self.grid[self.r][self.c-1] = self.grid[self.r][self.c-1] * 2
							self.grid[self.r][self.c] = 0
					self.c += 1

				elif direction == 'right':
					if self.r == 4:
						break
					if self.c <= 2:
						if self.grid[self.r][self.c+1] == self.grid[self.r][self.c]:
							self.grid[self.r][self.c+1] = self.grid[self.r][self.c+1] * 2
							self.grid[self.r][self.c] = 0
					self.c -= 1

			if direction == 'up':
				self.r += 1
				self.c = 0
			elif direction == 'down':
				self.r -= 1
				self.c = 0
			elif direction == 'left':
				self.r += 1
				self.c = 0
			elif direction == 'right':
				self.r += 1
				self.c = 0