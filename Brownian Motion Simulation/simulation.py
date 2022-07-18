import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy as sp
import random
import timeit

import simulation_functions as sf
import plot_functions as pf


def main():
    G = nx.read_edgelist('facebook_combined.txt',
                         create_using=nx.Graph(), nodetype=int)

    blue_amt, red_amt, n = 5, 5, 1000

    sf.update_G(G, blue_amt, red_amt)

    M, DT, DEV = sf.initialize_M(G), [], []

    for i in range(n):
        print(i)
        sf.update_M(G, M)
        sf.update_DEV(G, DEV)

    # pf.plot_M(M)
    # plt.savefig(f"Plots 2.0/M{0}_snap.png", dpi=1200)
    # plt.close()

    # pf.plot_DT(DEV)
    # plt.savefig(f"Plots 2.0/DT{0}_snap.png", dpi=1200)

    pf.plot_DEV(n, DEV)
    plt.savefig(f"Plots 2.0/DEV{0}_snap.png", dpi=1200)
    plt.close()

    pf.plot_DEGvBalls(G)
    plt.savefig(f"Plots 2.0/DEGvBalls{0}_snap.png", dpi=1200)
    plt.close()

    pf.plot_LogDegvBalls(G)
    plt.savefig(f"Plots 2.0/DegvBallsLog{0}_snap.png", dpi=1200)
    plt.close()

    pf.draw_graph(G)
    plt.savefig(f"Plots 2.0/Graph{0}_snap.png", dpi=1200)
    plt.close()


if __name__ == "__main__":
    main()
