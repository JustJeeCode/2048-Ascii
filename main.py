"""
2048 made with Python.
By JustJeeCode, 6/4/23.
"""

import platform
import os
from board import Board

# Getting os
user_os = platform.system()
if user_os == 'Windows': clear = 'cls'
else: clear = 'clear'

# Starting lines
os.system(clear)
board = Board()
board.update()

# Game loop
while True:
	# Updated board every round
	os.system(clear)
	board.update()
	board.display()
	board.score(True)

	# Movement
	if board.check() >= 1:
		print("Board Movement:\n[W] = Up.\n[S] = Down.\n[A] = Left.\n[D] = Right.\n[ANY KEY] = Quit.\n")
		player_inp = input(">>> ").lower()

		# Board movement
		if player_inp == 'w':
			board.move('up')
			board.merge('up')
			board.move('up')
		elif player_inp == 's':
			board.move('down')
			board.merge('down')
			board.move('down')
		elif player_inp == 'a':
			board.move('left')
			board.merge('left')
			board.move('left')
		elif player_inp == 'd':
			board.move('right')
			board.merge('right')
			board.move('right')
		else:
			break
	else:
		# If no more possible moves
		os.system(clear)
		board.display()
		print('\nGame Over!')
		board.score(False)
		break
