import networkx as nx
import numpy as np
import random


# add red_amt balls and blue_amt balls to G
def add_to_G(G, blue_amt: int, red_amt: int) -> None:
    for node in list(G.nodes):
        blue_balls = ["{}_{}".format(
            "blue",
            j + (node * blue_amt)) for j in range(blue_amt)]

        red_balls = ["{}_{}".format(
            "red",
            j + (node * red_amt)) for j in range(red_amt)]

        G.nodes[node]['Balls'] = blue_balls + red_balls


# initialize M
def initialize_M(G, M: dict) -> None:
    for node in list(G.nodes):
        for ball_ID in G.nodes[node]['Balls']:
            M[ball_ID] = [node]


def add_to_M(G, V_2: list, M: dict) -> None:
    for current_node in V_2:
        for neighbor_node in list(G.neighbors(current_node)):
            ball_curr = random.choice(G.nodes[current_node]['Balls'])
            ball_neigh = random.choice(G.nodes[neighbor_node]['Balls'])

            if ball_curr.startswith("red") and ball_neigh.startswith("blue"):
                G.nodes[current_node]['Balls'].remove(ball_curr)
                G.nodes[neighbor_node]['Balls'].append(ball_curr)

                M[ball_curr].append(neighbor_node)

            elif ball_curr.startswith("blue") and ball_neigh.startswith("red"):
                G.nodes[neighbor_node]['Balls'].remove(ball_neigh)
                G.nodes[current_node]['Balls'].append(ball_neigh)

                M[ball_neigh].append(current_node)


def add_to_DT(G, M: dict, i: int, DT: dict) -> None:
    for ball_ID in M:
        if ball_ID.startswith("red"):
            start_node = M[ball_ID][0]
            end_node = M[ball_ID][-1]

            displacement = nx.shortest_path_length(G, start_node, end_node)

            if ball_ID not in DT:
                DT[ball_ID] = []

            DT[ball_ID].append((i, displacement))


# appends calculated standard deviation of red balls contained by each node to DEV list
def add_to_DEV(G, i: int, DEV: list) -> None:
    red_balls_list = []

    for node in list(G.nodes):
        red_balls_count = 0

        for ball in G.nodes[node]['Balls']:
            if ball.startswith("red"):
                red_balls_count += 1

        red_balls_list.append(red_balls_count)

    std_dev = np.std(red_balls_list)
    DEV.append((i, std_dev))
