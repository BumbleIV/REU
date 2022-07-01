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


# bar plot depicting number of times each ball moves between node
def plot_M(M: dict) -> None:
    # Plot Configuration
    # plt.rcParams["figure.figsize"] = [10000000, 10]
    # plt.rcParams["figure.autolayout"] = True
    plt.xlabel('Node_ID')
    plt.ylabel('Number of Moves')
    plt.title('Number of Times Each Ball Moves Between Nodes')

    # Bar Plot
    for ball_ID, move_list in M.items():
        if ball_ID.startswith("red"):
            x = ball_ID
            y = len(move_list) - 1
            plt.bar(x, y, color='r', label=ball_ID, width=5)
            plt.text(x, y, str(y), ha='center', va='bottom')

    plt.xticks(rotation=90)
    # plt.legend()
    plt.show()


# plot the displacement of each ball in each node
def plot_DT(DT: dict) -> None:
    # Plot Configuration
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel('Iterations')
    plt.ylabel('Distance')
    plt.title('Distance of Red Balls from Node at Each Iteration')

    for ball_ID, distance_list in DT.items():
        x, y = zip(*distance_list)
        plt.plot(x, y, label=ball_ID)

    # plt.legend()
    plt.show()


# custom plots of standard deviation of red balls in each node
def plot_DEV(DEV: list) -> None:
    # Plot Configuration
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True
    plt.xlabel('Iterations')
    plt.ylabel('Standard Deviation')
    plt.title(
        'Standard Deviation of Red Balls Contained by All Nodes at Each Iteration')

    x, y = zip(*DEV)

    # Standard Deviation Plot
    plt.plot(x, y, 'ro-',
             label="Standard Deviation",
             linewidth=0.5,
             markersize=0.5)

    # Line of Best Fit Plot
    # slope, intercept = np.polyfit(x, y, 1)
    # plt.plot(x, slope * x + intercept, 'b-',
    #          label="Line of Best Fit",
    #          linewidth=0.5)

    # Mean Standard Deviation Plot
    mean_std_dev = np.mean(y)

    plt.axhline(mean_std_dev, color='g',
                label="Average Standard Deviation",
                linewidth=2.0)

    plt.legend()
    plt.show()
