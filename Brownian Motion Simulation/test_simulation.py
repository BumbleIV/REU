import unittest
import networkx as nx
import random

import simulation as sim
import helper_functions as hf


G = nx.gnm_random_graph(n=random.randint(5, 10),
                        m=random.randint(5, 10))

M = sim.RedBallBlueBall(G, n=100, blue_amt=5, red_amt=5)


class TestSimulation(unittest.TestCase):
    # test that M dict correctly records ball movement by asserting node \
    # containing most balls in M dict is equal to node containing most balls in G graph
    def test_node_max_balls(self):
        self.assertEqual(hf.max_balls_graph(G), hf.max_balls_map(M))

    # select random node from G and track number of balls 
    def test_map_tracking(self):
        pass

    # validate that blue_balls in M dict do not move whatsoever
    def test_blue_balls_not_moving(self):
        (self.assertEqual(len(M[i]), 1)
         for i in M
         if i.startswith("blue"))

    # asserts if nodes of red_ball that has moved more than once has touched have edges between them
    def test_red_balls_moving(self):
        for i in M:
            if i.startswith("red") and len(M[i]) > 1:
                for j in range(len(M[i]) - 1):
                    self.assertTrue(G.has_edge(M[i][j], M[i][j+1]))

    # validate sampling of two balls is random
    def test_random_sampling(self):
        pass


# validate that the randomization of sampling a node's ball is working
# map[node_ID] = [ball_ID, ball_ID, ...]
# check for sufficient randomness of sampling a node's ball
# focus on the blue balls since they are fixed
# fraction of red balls sampled vs blue balls for a given x_amt of node
# check if most blue balls be sampled at least once (maybe 20=n iterations)
# with more neighbors will a node be sampled more
# at end of n iterations for given node 2kn balls will be sampled
# you can manually pick a node with k amount of neighbors
# check for expected size
if __name__ == '__main__':
    unittest.main()
