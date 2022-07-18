from tkinter import font
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy as sp

from networkx.drawing.nx_agraph import graphviz_layout


# prints input map
def print_map(M: dict) -> None:
    for key, value in M.items():
        print("{}: {}".format(key, value) + "\n")


# draws graph G
def draw_graph(G) -> None:
    plt.rcParams.update(plt.rcParamsDefault)

    fig, ax = plt.subplots()

    num_nodes = len(G.nodes())
    num_edges = len(G.edges())

    text = 'Number of Nodes: {}\nNumber of Edges: {}\nFacebook Network from snap.stanford.edu'.format(
        num_nodes, num_edges)

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.25)

    ax.text(0.00, 0.95, text, fontsize=6, ha='left',
            va='top', transform=plt.gca().transAxes, bbox=props)

    node_sizes = [(len(G.nodes[node]['Red Balls']) +
                   len(G.nodes[node]['Blue Balls'])) ** 1.5 for node in G.nodes]

    pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos, node_size=node_sizes,
                     node_color='red',
                     edge_color='black',
                     width=0.05,
                     alpha=0.1,
                     with_labels=False,
                     ax=ax)

    # plt.show()


# Bar Plot depicting number of times each ball moves between node
def plot_M(M: dict) -> None:
    plt.rcParams.update(plt.rcParamsDefault)
    plt.xlabel('Ball ID')
    plt.xticks(rotation=90, fontsize=4)
    plt.ylabel('Number of Moves')
    plt.title('Number of Times Each Ball Moves Between Nodes')

    x = [key for key in M if key.startswith("red")]
    y = [len(M[key]) - 1 for key in x]

    # plt.show()


# Scatter Plot depicting Average Displacement from given starting node of Red Balls in M at each iteration
def plot_DT(n: int, DT: list) -> None:
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('ggplot')
    plt.xlabel('Iterations')
    plt.ylabel('Average Displacement')
    plt.title('Average Displacement of Red Balls')

    x = range(n)
    y = DT

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

    plt.legend(loc='lower right', fontsize=3)

    # plt.show()


# Scatter Plot of standard deviation of red balls in each node
def plot_DEV(n: int, DEV: list) -> None:
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('ggplot')
    plt.xlabel('Iterations')
    plt.ylabel('Standard Deviation')
    plt.title(
        'Standard Deviation of Red Balls in Nodes')

    x = np.arange(n)
    y = DEV

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

    plt.legend(loc='lower right', fontsize=3)
    # plt.show()


# Plot depicting degree of a node in G vs. number of Balls contained by node (using ggplot2 and alphablending)
def plot_DEGvBalls(G):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('ggplot')
    plt.xlabel('Degree of Node')
    plt.ylabel('Number of Balls')
    plt.title('Degree of Node vs. Number of Balls in Node')

    x = [G.degree(node) for node in G.nodes()]
    y = [len(G.nodes[node]['Red Balls']) + len(G.nodes[node]['Blue Balls'])
         for node in G.nodes()]

    plt.plot(x, y, 'ro',
             label='Degree of Node vs. Number of Balls',
             linewidth=0,
             markersize=20,
             markeredgewidth=0.0,
             alpha=0.025)


# Plot depicting degree of a node in G vs. number of Balls contained by node
def plot_LogDegvBalls(G):
    plt.rcParams.update(plt.rcParamsDefault)
    plt.style.use('ggplot')
    plt.xlabel('Degree of Node (Log Scale)')
    plt.xscale('log')
    plt.ylabel('Number of Balls')
    plt.title('Degree of Node vs. Number of Balls in Node')

    for node in G.nodes():
        x = G.degree(node)
        y = len(G.nodes[node]['Red Balls']) + len(G.nodes[node]['Blue Balls'])

        plt.plot(x, y, 'ro',
                 label='Degree of Node vs. Number of Balls',
                 linewidth=0,
                 markersize=20,
                 markeredgewidth=0.0,
                 alpha=0.025)
