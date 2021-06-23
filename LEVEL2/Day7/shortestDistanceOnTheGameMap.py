def search(maps, visited, queue, dist):
	rowl = [0,0,-1,1]
	coll = [1,-1,0,0]
	dist[0][0] = 1
	visited[0][0] = True
	
	while queue:
		cord = queue.pop(0)
		for i in range(4):
			nrow = cord[0] + rowl[i]
			ncol = cord[1] + coll[i]
			if nrow >= 0  and nrow < len(maps) and ncol >=0 and ncol < len(maps[0]):
				if maps[nrow][ncol] == 1 and visited[nrow][ncol] == False:
					visited[nrow][ncol] = True
					queue.append((nrow,ncol))
					dist[nrow][ncol] = dist[cord[0]][cord[1]] + 1
					if nrow==len(maps)-1 and ncol == len(maps[0])-1:
						return dist[nrow][ncol]
	return -1 		
def solution(maps):
	queue = [(0,0)]
	mov = [1]
	visited = []
	dist = []
	for i in maps:
		tmp = []
		tmp2 = []
		for j in i:
			tmp.append(False)
			tmp2.append(0)
		visited.append(tmp)
		dist.append(tmp2)
	answer = search(maps, visited, queue, dist)
	return answer