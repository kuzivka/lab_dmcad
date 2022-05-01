import networkx as nx
import numpy as np

def is_isomorphic(graph1, graph2):
    G1 = nx.from_numpy_matrix(graph1)
    G2 = nx.from_numpy_matrix(graph2)
    isomorphic = nx.is_isomorphic(G1,G2)
    print("Are graphs isomorphic? \t")
    return isomorphic


graph1 = np.array([[0, 0, 1, 1],
                   [0, 0, 1, 0],
                   [1, 1, 0, 1],
                   [1, 0, 1, 0]])

graph2 = np.array([[0, 1, 1, 1],
                   [1, 0, 0, 0],
                   [1, 0, 0, 1],
                   [1, 0, 1, 0]])


print(is_isomorphic(graph1,graph2))
