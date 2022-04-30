import sys
import numpy as np

INF = 9999999


class Graph: 
	def __init__(self, V, G):
		self.V = V
		self.G = G

	def prim(self):
		selected = [0] * self.V
		no_edge = 0
		selected[0] = True
		min_tree = 0
		print("Edge : Weight")
		while (no_edge < self.V - 1):
			minimum = INF
			x = 0
			y = 0
			for i in range(V):
				if selected[i]:
					for j in range(self.V):
						if ((not selected[j]) and self.G[i][j]):  
							if minimum > self.G[i][j]:
								minimum = self.G[i][j]
								x = i
								y = j
			print(str(x) + "-" + str(y) + ":" + str(self.G[x][y]))
			min_tree += self.G[x][y]
			selected[y] = True
			no_edge += 1
		print("Min Tree: " + str(min_tree))

if __name__=='__main__':
	V = 8
	G = [[0, 3, 0, 0, 0, 34, 0, 80],
         [3, 0, 0, 1, 0, 0, 0, 68],
         [0, 0, 0, 0, 23, 0, 12, 0],
         [0, 1, 0, 0, 53, 0, 0, 39],
        [0, 0, 23, 53, 0, 0, 68, 14],
        [34, 0, 0, 0, 0, 0, 0, 25],
        [0, 0, 12, 0, 68, 0, 0, 99],
        [80, 68, 0, 39, 14, 25, 99, 0]]	

	graph = Graph(V,G)
	graph.prim()
