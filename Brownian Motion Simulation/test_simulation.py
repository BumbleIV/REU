import unittest
import networkx as nx
import random

import simulation as sim
import helper_functions as hf


G = nx.gnm_random_graph(n=random.randint(5, 10),
                        m=random.randint(5, 10))

n = 100
blue_amt = 5
red_amt = 5

M, ND, DEV = sim.RedBallBlueBall(G, n, blue_amt, red_amt)


class TestSimulation(unittest.TestCase):
    # assertEqual that blue balls in M dict do not move whatsoever
    def test_blue_balls_movement(self):
        for ball_ID in M:
            if ball_ID.startswith("blue"):
                node_count = len(M[ball_ID])

                self.assertEqual(node_count, 1)

    # assertTrue that the nodes red balls travel across have edges between them
    def test_red_balls_movement(self):
        for ball_ID in M:
            node_count = len(M[ball_ID])

            if ball_ID.startswith("red") and node_count > 1:
                for i in range(node_count - 1):
                    node_curr = M[ball_ID][i]
                    node_next = M[ball_ID][i + 1]

                    self.assertTrue(G.has_edge(node_curr, node_next))


if __name__ == '__main__':
    unittest.main()
