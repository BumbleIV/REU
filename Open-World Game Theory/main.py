import networkx as nx
import matplotlib.pyplot as plt
import random

# Simulating Prisoner’s Dilemma transactions on network of decision-making agents

# Network imported from https://snap.stanford.edu/data/ego-Facebook.html


def hello_input(input: str) -> str:
    return "Hello " + input


def main():
    G = nx.read_edgelist('facebook_combined.txt',
                         create_using=nx.Graph(),
                         nodetype=int)

    print(nx.info(G))

    sp = nx.spring_layout(G)
    nx.draw(G,
            pos=sp,
            with_labels=False,
            node_size=10,)

    plt.show()
    


if __name__ == "__main__":
    main()
