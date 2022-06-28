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
# 2. Attribute each node in G a node_ID, blue_amt and red_amt balls
# 3. Enter blue_IDs and red_IDs into M as keys with empty lists as values
# 4. Copy G into V_2 then randomize (and fix) the order of nodes in V_2
# 5. Select current_node and neighbor_node from V_2
# 6. Randomly sample 1 ball each from current_node and neighbor_node then apply following rules:
#    a. If both balls sampled are the same color, the no transaction occurs
#    b. If both balls sampled are different colors, the red ball is removed from its owner node and given to the opposing node
#       b1. Append the node_ID of V_2 that the red ball is moved to into the list of values of the key of the ball_ID
# 7. Repeat steps 6 until all neighbor_node of current_node are visited
# 8. Select next current_node in V_2
# 9. Repeat steps 6-8 until n iterations are completed
# 10. Return M


from matplotlib import markers
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import random

import helper_functions as hf


def RedBallBlueBall(G, n: int = 100, blue_amt: int = 5, red_amt: int = 5) -> dict:
    M = {}

    for i in G:
        blue_balls = ["{}_{}".format(
            "blue",
            j + (i * blue_amt)) for j in range(blue_amt)]

        red_balls = ["{}_{}".format(
            "red",
            j + (i * red_amt)) for j in range(red_amt)]

        G.nodes[i]['Balls'] = blue_balls + red_balls

        G.nodes[i]['node_ID'] = i

        for ball_ID in G.nodes[i]['Balls']:
            M[ball_ID] = [G.nodes[i]['node_ID']]

    V_2 = list(G.nodes)
    random.shuffle(V_2)

    std_dev_list = []
    for i in range(n):
        for current_node in V_2:
            for neighbor_node in list(G.neighbors(current_node)):
                ball_curr = random.choice(G.nodes[current_node]['Balls'])
                ball_neigh = random.choice(G.nodes[neighbor_node]['Balls'])

                if ball_curr.startswith("red") and ball_neigh.startswith("blue"):
                    G.nodes[current_node]['Balls'].remove(ball_curr)
                    G.nodes[neighbor_node]['Balls'].append(ball_curr)

                    M[ball_curr].append(G.nodes[neighbor_node]['node_ID'])

                elif ball_curr.startswith("blue") and ball_neigh.startswith("red"):
                    G.nodes[neighbor_node]['Balls'].remove(ball_neigh)
                    G.nodes[current_node]['Balls'].append(ball_neigh)

                    M[ball_neigh].append(G.nodes[current_node]['node_ID'])

        red_balls_list = hf.red_balls_list(G, V_2)
        std_dev = np.std(red_balls_list)
        std_dev_list.append(std_dev)

        plt.plot(i, std_dev, '-o',  markersize=0.5)

        print("Standard Deviation at {}: {}".format(i, std_dev))
        print(red_balls_list)
        print("\n")

    print(np.average(std_dev_list))
    plt.show()

    return M


def main():
    G = nx.gnm_random_graph(n=random.randint(10, 15),
                            m=random.randint(10, 15))
    n = 5000
    blue_amt, red_amt = 5, 5

    M = RedBallBlueBall(G, n, blue_amt, red_amt)


if __name__ == "__main__":
    main()
