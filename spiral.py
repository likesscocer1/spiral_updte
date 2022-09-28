
size = 102


def spiral(size):
	listas = [[],[],[],[]]
	coordinates = [2,0]

	right = True
	up = False
	left = False
	down = False

	count = 0
	time_to_move = 1

	for i in range(1, size+1):
		if right:
			listas[coordinates[0]].append(i)
			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])			
			if i != 1:
				count += 1
			if count == time_to_move:
				right = False
				up = True
				count = 0
				continue

		if up:
			coordinates[0] -=1
			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])
			if coordinates[0] < 0:
				listas.insert(0,[])
				coordinates[0] = 0
			listas[coordinates[0]].append(i)
			if i == size:
				while len(listas[coordinates[0]]) != len(listas[coordinates[0]+1]):
					listas[coordinates[0]].insert(0,'')
			count += 1
			if count == time_to_move:
				up = False
				left = True
				count = 0
				time_to_move += 1
				continue

		if left:
			listas[coordinates[0]].insert(0,i)

			if i == size:
				if len(listas[coordinates[0]])<len(listas[coordinates[0]+1]) or len(listas[coordinates[0]])==len(listas[coordinates[0]+1]):
					while len(listas[coordinates[0]]) != len(listas[coordinates[0]+1]):
						listas[coordinates[0]].insert(0,'')
				else:
					coordinates[0] +=1
					for row in listas[coordinates[0]:]:
						index = listas.index(row)
						listas[index].insert(0,'')
			count += 1
			if count == time_to_move:
				left = False
				down = True
				count = 0
				continue

		if down:
			coordinates[0] +=1
			listas[coordinates[0]].insert(0,i)
			if i == size:
				coordinates[0] +=1
				for row in listas[coordinates[0]:]:
					index = listas.index(row)
					listas[index].insert(0,'')
			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])
			count += 1
			if count == time_to_move:
				down = False
				right = True
				count = 0
				time_to_move +=1
				continue
	return listas
	



spiral = spiral(size)

# print finals results
for i in spiral:
	for j in i:
		print(str(j).rjust(3), end=' ')
	print()