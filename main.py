import networkx as nx
from pip import main

G = nx.Graph()
H = nx.Graph()

# testing valid variable types for add_node
G.add_node(1)
G.add_node("strings")
G.add_node(2.03434)

print(list(G.nodes))

print("")
