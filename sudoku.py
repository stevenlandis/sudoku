#a sudoku puzzle solver

#board = [9, [], [], [], [], [], [], [], 5, 3, [], 8, [], [], [], 6, [], 2, [], 6, [], [], 5, [], [], 8, [], [], 2, [], 8, 4, 1, [], 3, [], [], [], [], [], [], [], [], [], [], [], 7, [], 6, 3, 9, [], 2, [], [], 8, [], [], 1, [], [], 4, [], 6, [], 5, [], [], [], 2, [], 3, 2, [], [], [], [], [], [], [], 8]

def getBoard():
	board = []
	for _ in range(9):
		line = input()
		for c in line:
			if c == '0' or c == ' ':
				board.append([])
			else:
				board.append(int(c))
	return board

def isPossible(board, n, x, y):
	#check inside square
	X = (x//3) * 3
	Y = (y//3) * 3
	for i in range(X, X+3):
		for j in range(Y, Y+3):
			if board[i + 9*j] == n:
				return False

	#check horizontal line
	for i in range(9):
		if board[i + 9*y] == n:
			return False

	#check vertical line
	for i in range(9):
		if board[x + 9*i] == n:
			return False

	#if flow has made it this far:
	return True

def possibleList(board, x, y):
	list = []
	for i in range(1,10):
		if isPossible(board, i, x, y):
			list.append(i)
	if len(list) == 0:
		print("uh oh at x:",x,", y:",y)
	return list

def simplify(board):
	changed = False
	#check for lists with only one member
	for i in range(len(board)):
		if type(board[i]) == list and len(board[i]) == 1:
			setBoardValue(board, board[i][0], i)
			return True

	#check squares for a number only in one list
	for X in range(0,9,3):
		for Y in range(0,9,3):
			for k in range(1, 10):
				appearances = 0
				ai = None
				for i in range(X, X+3):
					for j in range(Y, Y+3):
						if type(board[i + 9*j]) == list and k in board[i + 9*j]:
							appearances += 1
							ai = i + 9*j
				if appearances == 1:
					setBoardValue(board, k, ai)
					return True

	#check horizontal lines
	for y in range(9):
		for k in range(1,10):
			appearances = 0
			ai = None
			for x in range(9):
				if type(board[x + 9*y]) == list and k in board[x + 9*y]:
					appearances += 1
					ai = x + 9*y
			if appearances == 1:
				setBoardValue(board, k, ai)
				return True

	#check vertical lines
	for x in range(9):
		for k in range(1,10):
			appearances = 0
			ai = None
			for y in range(9):
				if type(board[x + 9*y]) == list and k in board[x + 9*y]:
					appearances += 1
					ai = x + 9*y
			if appearances == 1:
				setBoardValue(board, k, ai)
				return True
	return changed

def setBoardValue(board, n, i):
	#print("Setting x:",i%9,", y:",i//9,"to",n)
	board[i] = n

def updateLists(board):
	for i in range(len(board)):
		if type(board[i]) == list:
			board[i] = possibleList(board, i%9, i//9)


def printBoard(board):
	res = ""
	for i in range(len(board)):
		if type(board[i]) == list:
			res += ' '
		else:
			res += str(board[i])
		if i%9 == 8:
			if i != 80:
				res += '\n'
			if i%27 == 26 and i != 80:
				res += '-'*21 + '\n'
		else:
			res += ' '
			if i%3 == 2:
				res += '| '
	print(res)

print("Enter the board (use spaces or 0 for blanks and a newline for each line):")
board = getBoard()

print("\nYou entered:")
printBoard(board)

i = 0
changed = True
while changed and i < 100:
	i += 1
	updateLists(board)
	changed = simplify(board)

print("\nSolved Board:")
printBoard(board)