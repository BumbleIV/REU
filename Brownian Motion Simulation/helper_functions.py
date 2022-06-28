import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

# prints map


def print_map(M: dict) -> None:
    for key, value in M.items():
        print("{}: {}".format(key, value) + "\n")


def draw_graph(G) -> None:
    nx.draw(G, with_labels=True)
    plt.show()

# returns node with most balls in map as tuple (node, max_balls)


def max_balls_map(M: dict) -> tuple:
    map = {}

    for ball_ID in M:
        last_node = M[ball_ID][-1]

        if last_node in map:
            map[last_node] += 1
        else:
            map[last_node] = 1

    node = max(map, key=map.get)
    return (node, map[node])


# returns node with most balls in graph as tuple (node, max_balls)
def max_balls_graph(G) -> tuple:
    max_balls = 0
    max_node = None

    for i in G:
        if len(G.nodes[i]['Balls']) > max_balls:
            max_balls = len(G.nodes[i]['Balls'])
            max_node = i

    return (max_node, max_balls)

# returns a numpy array of ints containing number of red balls in each node of input list


def red_balls_list(G, V: list) -> list:
    red_balls_list = []

    for i in V:
        count = 0
        for ball in G.nodes[i]['Balls']:
            if ball.startswith("red"):
                count += 1
        red_balls_list.append(count)

    return red_balls_list
