from sys import maxsize
from itertools import permutations
V = 6

def travellingSalesmanProblem(graph, s):

	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:
		current_pathweight = 0

		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		min_path = min(min_path, current_pathweight)
	return min_path


if __name__ == "__main__":

	graph = [[0, 0, 69, 60, 10, 20],
                [0, 0, 0, 31, 39, 2],
		[69, 0, 0, 0, 59, 0],
                 [60, 31, 0, 0, 0, 36],
                 [10, 39, 59, 0, 0, 79],
                [20, 2, 0, 36, 79, 0]]
	s = 0
	print('Distance: ',travellingSalesmanProblem(graph, s))
