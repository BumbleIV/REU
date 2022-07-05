import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import random

import simulation_functions as sf
import helper_functions as hf


def RedBallBlueBall(G, n: int, blue_amt: int, red_amt: int) -> dict:
    M = {}
    DT = []
    DEV = []

    sf.add_to_G(G, blue_amt, red_amt)

    sf.initialize_M(G, M)

    V_2 = list(G.nodes)
    random.shuffle(V_2)

    for i in range(n):
        sf.add_to_M(G, V_2, M)
        sf.add_to_DT(G, M, i, DT)
        sf.add_to_DEV(G, i, DEV)

    return M, DT, DEV


def main():
    G = nx.gnm_random_graph(n=15,
                            m=10)
    n = 10000
    blue_amt, red_amt = 5, 5

    for i in range(3):
        M, DT, DEV = RedBallBlueBall(G, n, blue_amt, red_amt)

        # hf.draw_graph(G)
        # print(G.number_of_nodes())
        # print(G.number_of_edges())

        # hf.plot_M(M)
        hf.plot_DT(DT)
        # hf.plot_DEV(DEV)

        # hf.print_map(M)
        # hf.print_map(DT)
        # hf.print_map(DEV)

        plt.savefig(f"Plots/DT/DT{i}.png")

        plt.pause(3)
        plt.close()


if __name__ == "__main__":
    main()
