import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# prints map
def print_map(M: dict) -> None:
    for key, value in M.items():
        print("{}: {}".format(key, value) + "\n")


# draws graph
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


# returns node with most balls in graph as tuple (max_node, max_balls)
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


# custom plots of standard deviation of red balls in each node
def std_dev_plot(x, y) -> None:
    # Plot Configuration
    plt.rcParams["figure.figsize"] = [1000000, 10]
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel('Iterations')
    plt.ylabel('Standard Deviation')
    plt.title(
        'Standard Deviation of Red Balls Contained by All Nodes at Each Iteration')

    # Standard Deviation Plot
    plt.plot(x, y, 'ro-',
             label="Standard Deviation",
             linewidth=0.5,
             markersize=0.5)

    # Line of Best Fit Plot
    m, b = np.polyfit(x, y, 1)
    line = m * x + b

    plt.plot(x, line, 'b--',
             label="Line of Best Fit",
             linewidth=2.0)

    # Mean Standard Deviation Plot
    mean_std_dev = np.mean(y)

    plt.axhline(mean_std_dev, color='g',
                label="Average Standard Deviation",
                linewidth=2.0)

    plt.legend()
    plt.show()
