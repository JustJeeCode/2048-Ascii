"""
2048 made with Python.
By JustJeeCode, 6/4/23.
"""

import os
from board import Board

clear = 'clear' # If running a windows change this variable to 'cls'

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
			board.up()
			board.merge_up()
			board.up()
		elif player_inp == 's':
			board.down()
			board.merge_down()
			board.down()
		elif player_inp == 'a':
			board.left()
			board.merge_left()
			board.left()
		elif player_inp == 'd':
			board.right()
			board.merge_right()
			board.right()
		else:
			break
	else:
		# If no more possible moves
		os.system(clear)
		board.display()
		print('\nGame Over!')
		board.score(False)
		break
