import networkx as nx
import numpy as np
import random
import timeit


# attribute red_amt balls and blue_amt balls to G.nodes
def update_G(G, blue_amt: int, red_amt: int) -> None:
    for node in list(G.nodes):
        blue_balls = ["blue_{}".format(j + (node * blue_amt))
                      for j in range(blue_amt)]

        red_balls = ["red_{}".format(j + (node * red_amt))
                     for j in range(red_amt)]

        G.nodes[node]['Blue Balls'] = blue_balls
        G.nodes[node]['Red Balls'] = red_balls


# initialize M
def initialize_M(G) -> dict:
    M = {}

    for node in list(G.nodes):
        for ball_ID in (G.nodes[node]['Red Balls'] + G.nodes[node]['Blue Balls']):
            M[ball_ID] = [node]

    return M


def update_M(G, M) -> dict:
    V_2 = list(G.nodes)
    random.shuffle(V_2)

    for current_node in V_2:
        neighbor_nodes = list(G.neighbors(current_node))
        neighbor_node = random.choice(neighbor_nodes)

        balls_curr = G.nodes[current_node]['Red Balls'] + \
            G.nodes[current_node]['Blue Balls']
        balls_neigh = G.nodes[neighbor_node]['Red Balls'] + \
            G.nodes[neighbor_node]['Blue Balls']

        ball_curr = random.choice(balls_curr)
        ball_neigh = random.choice(balls_neigh)

        if ball_curr.startswith("red") and ball_neigh.startswith("blue"):
            G.nodes[current_node]['Red Balls'].remove(ball_curr)
            G.nodes[neighbor_node]['Red Balls'].append(ball_curr)

            M[ball_curr].append(neighbor_node)

        elif ball_curr.startswith("blue") and ball_neigh.startswith("red"):
            G.nodes[neighbor_node]['Red Balls'].remove(ball_neigh)
            G.nodes[current_node]['Red Balls'].append(ball_neigh)

            M[ball_neigh].append(current_node)


# Calculate the Average Displacement (length away a ball is from starting node) of all Red Balls at each iteration
def update_DT(G, M: dict, DT: list) -> None:
    displacement_list = []

    for ball_ID in M:
        if ball_ID.startswith("red"):
            start_node = M[ball_ID][0]
            end_node = M[ball_ID][-1]

            displacement = nx.shortest_path_length(G, start_node, end_node)
            displacement_list.append(displacement)

    mean_dt = np.mean(displacement_list)
    DT.append(mean_dt)


# Calculate the Standard Deviation of Red Balls contained by all nodes at a given iteration
def update_DEV(G, DEV: list) -> None:
    red_balls_list = []

    for node in list(G.nodes):
        red_balls_count = len(G.nodes[node]['Red Balls'])
        red_balls_list.append(red_balls_count)

    std_dev = np.std(red_balls_list)
    DEV.append(std_dev)
