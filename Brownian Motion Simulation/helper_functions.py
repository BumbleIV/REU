from tkinter import font
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# prints input map
def print_map(M: dict) -> None:
    for key, value in M.items():
        print("{}: {}".format(key, value) + "\n")


# draws input network (graph)
def draw_graph(G) -> None:
    nx.draw(G, with_labels=True)
    plt.show()


# returns a tuple (node_ID containing the most balls: str, number of balls: int) given a dict
def node_most_balls(M: dict) -> tuple:
    map = {}

    for ball_ID in M:
        last_node = M[ball_ID][-1]

        if last_node in map:
            map[last_node] += 1
        else:
            map[last_node] = 1

    node_ID = max(map, key=map.get)
    balls_count = map[node_ID]

    return (node_ID, balls_count)


# Bar Plot depicting number of times each ball moves between node
def plot_M(M: dict) -> None:
    plt.xlabel('Node_ID')
    plt.ylabel('Number of Moves')
    plt.title('Number of Times Each Ball Moves Between Nodes')

    # Bar Plot
    for ball_ID, move_list in M.items():
        if ball_ID.startswith("red"):
            x = ball_ID
            y = len(move_list) - 1
            plt.bar(x, y, label=ball_ID, color='r')
            plt.text(x, y, str(y), ha='center', va='bottom', fontsize=3)

    plt.xticks(fontsize=6, rotation=90)
    # plt.show()


# Scatter Plot depicting Average Displacement from given starting node of Red Balls in M at each iteration
def plot_DT(DT: list) -> None:
    plt.style.use('ggplot')
    plt.xlabel('Iterations')
    plt.ylabel('Average Displacement')
    plt.title('Average Displacement of All Red Balls')

    x, y = zip(*DT)

    plt.plot(x, y, 'ro-',
             label='Average Displacement',
             linewidth=0.5,
             markersize=0.5)

    poly = np.poly1d(np.polyfit(x, y, 1))
    plt.plot(x, poly(x), 'y-',
             label='Linear Fit',
             linewidth=2.0)

    mean_displacement = np.mean(y)
    plt.axhline(mean_displacement, color='k',
                label='Mean Displacement',
                linewidth=2.0)

    plt.legend()
    # plt.show()


# Scatter Plot of standard deviation of red balls in each node
def plot_DEV(DEV: list) -> None:
    plt.style.use('ggplot')
    plt.xlabel('Iterations')
    plt.ylabel('Standard Deviation')
    plt.title(
        'Standard Deviation of Red Balls Contained by All Nodes at Each Iteration')

    x, y = zip(*DEV)

    plt.plot(x, y, 'ro-',
             label="Standard Deviation",
             linewidth=0.5,
             markersize=0.5)

    poly = np.poly1d(np.polyfit(x, y, 1))
    plt.plot(x, poly(x), 'y-',
             label='Linear Fit',
             linewidth=2.0)

    mean_std_dev = np.mean(y)
    plt.axhline(mean_std_dev, color='k',
                label="Average Standard Deviation",
                linewidth=2.0)

    plt.legend()
    # plt.show()
