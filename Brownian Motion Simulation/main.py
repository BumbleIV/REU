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
# 2. Attribute each node in V a node_iD, blue_amt and red_amt balls
# 3. Copy V into V_2 then randomize (and fix) the order of nodes in V_2
# 4. Select V_2[i] as current_node
# 5. Record the current_node in M for each ball attributed to current_node
# 6. Select a neighbor_node of current_node
# 7. Record the neighbor_node in M for each ball attributed to neighbor_node
# 8. Randomly sample 1 ball each from current_node and neighbor_node then apply following rules:
#    a. If both balls sampled are the same color, the no transaction occurs
#    b. If both balls sampled are different colors, the red ball is removed from its owner node and given to the opposing node
# 9. Repeat steps 6-9 until all neighbor_node of current_node are visited
# 10. Select next current_node in V_2
# 11. Repeat steps 5-10 until n iterations are completed
# 12. Return M


# Use M for plots and data analysis.


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def RedBallBlueBall(G, n: int, blue_amt: int, red_amt: int) -> dict:
    # 1. Initialize M = {}
    M = {}

    # 2. Attribute each node in V blue_amt and red_amt balls
    for i in G:
        # create a list of blue balls with blue_amt amount of balls for each node
        blue_balls = ["{}_{}".format(
            "blue",
            j + (i * blue_amt)) for j in range(blue_amt)]

        # create a list of red balls with red_amt amount of balls for each node
        red_balls = ["{}_{}".format(
            "red",
            j + (i * red_amt)) for j in range(red_amt)]

        # attribute blue_balls and red_balls to node
        G.nodes[i]['Blue Balls'] = blue_balls
        G.nodes[i]['Red Balls'] = red_balls

    # 3. Copy V into V_2 then randomize (and fix) the order of nodes in V_2
    V_2 = list(G.nodes)  # V = list(G.nodes)
    random.shuffle(V_2)

    # 4. Select V_2[i] as current_node
    for i in range(n):
        pass

    return M


def main():
    # Input:

    # Network Model: G = (V, E)
    # generate a random graph with a random number of nodes and edges (between 5 and 30 for now)
    G = nx.gnm_random_graph(n=random.randint(5, 30), m=random.randint(5, 30))

    # Output:
    M = RedBallBlueBall(G, n=10, blue_amt=5, red_amt=5)

    # draw the graph
    # nx.draw(G, with_labels=False, node_size=10)
    # plt.show()

    # Insert Data Analysis Code of M here
    pass


if __name__ == "__main__":
    main()


# Could I possibly create a Ball object that has an ID, a color, and a list of nodes it has traveled to?
