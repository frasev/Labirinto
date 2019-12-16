class Labirinto():
	def __init__(self, grid, enter, leave):
		# The grid passed in input has a 0 in cells where it is
		# not possible to pass (they are obstacles), and a 1 where
		# it is possible to pass
		self.grid = grid
		self.enter = enter
		self.leave = leave

	def solve(self):
		moves = []
		
		# TODO: implement the solver
		# `moves` is a list of movements, from the
		# entrace to the exit.
		# Each move is represented using a character:
		#  'N': means to move north from the current position
		#  'S': means to move south from the current position
		#  'E': means to move east from the current position
		#  'W': means to move west from the current position
		labirinto = self.grid
		x = 0
		y = 1
		a = 0
		b = 1
		q = 0
		w = 1
		incroci = []
		last_incrocio = []
		passi = [[0,1]]
		z = 1
		
		while True:
			list = []
			if x == (len(labirinto)-1): 
				break
			pos = [x,y]
			pos_precedente = [a,b]
			confronto = [q,w]
			mosse = 0
			posizioni = []
			if labirinto[x+1][y] == 1:
				mosse+= 1
				if [x+1,y] not in passi:
					posizioni.append([x+1,y])
			if labirinto[x-1][y] == 1:
				mosse+= 1
				if [x-1,y] not in passi:
					posizioni.append([x-1,y])
			if labirinto[x][y+1] == 1:
				mosse+= 1
				if [x,y+1] not in passi:
					posizioni.append([x,y+1])
			if labirinto[x][y-1] == 1:
				mosse+= 1
				if [x,y-1] not in passi:
					posizioni.append([x,y-1])
			
			if mosse > 2:
				incroci.append([x,y])
				moves.append("incrocio"+str(z))
				z = z+1
			
			if len(posizioni) == 0: #Cerco l'ultimo punto da cui posso ripartire
				for i in range(0, len(incroci)):
					last_incrocio = incroci.pop()
					x = last_incrocio[0]
					y = last_incrocio[1]
					q = x
					w = y
					if labirinto[x+1][y] == 1:
						if [x+1,y] not in passi:
							posizioni.append([x+1,y])
					if labirinto[x-1][y] == 1:
						if [x-1,y] not in passi:
							posizioni.append([x-1,y])
					if labirinto[x][y+1] == 1:
						if [x,y+1] not in passi:
							posizioni.append([x,y+1])
					if labirinto[x][y-1] == 1:
						if [x,y-1] not in passi:
							posizioni.append([x,y-1])
					if len(posizioni) == 0:
						continue
					else: #rimuovo dalla lista le mosse sbagliate
						for p in range (0, moves.index("incrocio"+str(z-1-i))+1): 
							list.append(moves[p])
						z = z-1-i
						moves = []
						for i in list:
							moves.append(i)
						break
			else:
				for p in range (0, len(posizioni)):
					x = posizioni[p][0]
					y = posizioni[p][1]
					if [x,y] in passi:
						continue
					else:
						passi.append([x,y])
						break
			if confronto[0] == (x+1):
				a = x+1
				b = y
				moves.append("N")
			elif confronto[0] == (x-1):
				a = x-1
				b = y
				moves.append("S")
			elif confronto[1] == (y+1):
				b = y+1
				a = x
				moves.append("W")
			elif confronto[1] == (y-1):
				b = y-1
				a = x
				moves.append("E")
			q = x
			w = y
		for i in moves:
			if "incrocio" in i:
				moves.remove(i)
		return moves
	
	def __str__(self):
		ret = ''
		for r in self.grid:
			for cell in r:
				if cell == 0:
					ret += '█'
				elif cell == 1:
					ret += ' '
				else:
					ret += str(cell)
			ret += "\n"
		return ret
