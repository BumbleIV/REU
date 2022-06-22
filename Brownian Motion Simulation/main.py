# Input

# Network Model: G = (V, E)
# V = set of vertices (nodes)
# E = set of edges

# Number of Iterations: n

# Number of Blue Balls per node: blue (5 balls for now)
# Number of Red Balls per node: red (5 balls for now)

# Movement Record Dictionary: M = {}

# Output:
# M = {ball_ID: [node_ID, node_ID, ...], ball_ID: [node_ID, node_ID, ...], ...}


# Algorithm:
# 1. Initialize M = {}
# 2. Attribute each node in V input amount of blue and red balls
# 3. Randomize then fix the order of nodes to in V and record new order in V' = {}
# 4. Select V'[i] as current_node
# 5. Record the current_node in M for each ball attributed to current_node
# 6. Select a neighbor_node of current_node
# 7. Record the neighbor_node in M for each ball attributed to neighbor_node
# 8. Randomly sample 1 ball each from current_node and neighbor_node then apply following rules:
#    a. If both balls sampled are the same color, the no transaction occurs
#    b. If both balls sampled are different colors, the red ball is removed from its owner node and given to the opposing node
# 9. Repeat steps 6-9 until all neighbor_node of current_node are visited
# 10. Select next current_node in V'
# 11. Repeat steps 5-10 until n iterations are completed
# 12. Return M


# Use M for plots and data analysis.


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def RedBallBlueBall(G, n: int, blue: int, red: int) -> dict:
    # 1. Initialize M = {}
    M = {}

    # 2. Attribute each node in V input amount of blue and red balls
    for node in G.nodes():
        pass

    return M


def main():
    # generate a random graph with a random number of nodes and edges (between 5 and 30 for now)
    G = nx.gnm_random_graph(n=random.randint(5, 30), m=random.randint(5, 30))

    # draw the graph
    # nx.draw(G, with_labels=False, node_size=10)
    # plt.show()

    M = RedBallBlueBall(G, n=10, blue=5, red=5)


if __name__ == "__main__":
    main()
