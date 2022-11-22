import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph() 
g.add_edge(1, 2) # Adds edge from node 1 to node 2
g.add_edge(1, 3)
g.add_node(4) # Adds node 4
g.add_edge(1,4)
print("Edges:", g.edges())
print("Nodes:", g.nodes())
print("Neighbors of node 1:", list(g.neighbors(1)))

assert len(g.nodes()) == 4
assert len(g.edges()) == 3

nx.draw_networkx(g) 
plt.show()