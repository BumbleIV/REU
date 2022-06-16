import networkx as nx
import matplotlib.pyplot as plt
import random
import timeit


def main():
    # create empty undirected graphs
    # to create directed graphs, use nx.DiGraph()
    G = nx.Graph()
    H = nx.Graph()

    # variable type of node can be any "hashable" type
    # G.add_node(1)
    # G.add_node("strings")
    # G.add_node(2.03434)

    # add nodes from 3 to 9
    G.add_nodes_from(range(3, 10))

    # add edges
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)

    # add edges from 6 to 9
    G.add_edges_from([(6, 7), (6, 8), (6, 9)])

    # output nodes of G
    G_total_nodes = G.number_of_nodes()
    G_total_edges = G.number_of_edges()

    # print new lines
    print("\n" * 2)
    print("G Nodes ({}): ".format(G_total_nodes),  list(G.nodes))
    print("G Edges ({}): ".format(G_total_edges), list(G.edges))

    # views
    print("G.nodes(): ", G.nodes)
    print("G.edges(): ", G.edges)
    print("G.degree(): ", G.degree)
    print("G.adj(): ", G.adj)

    # add attributes to nodes
    for node in G.nodes:
        G.nodes[node]['smoking'] = False
        G.nodes[node]['weight'] = random.choice(range(100, 300))
    G.nodes[1]['smoking'] = True

    # print attributes of nodes
    print("\n" * 2)
    print("G.nodes.data(): ", G.nodes.data())

    # add attributes to edges
    for edge in G.edges:
        G.edges[edge]['strength'] = round(random.random(), 2)

    # print attributes of edges
    print("\n" * 2)
    print("G.edges.data(): ", G.edges.data())

    # draw graph
    nx.draw(G)
    plt.show()


if __name__ == '__main__':
    # start = timeit.timeit()

    main()

    end = timeit.timeit()

    print("\n" * 2)
    # print("Time: ", end - start)
