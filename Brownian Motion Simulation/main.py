# Input

# Network Model: G = (V, E)
# V = set of vertices (nodes)
# E = set of edges

# Number of Iterations: n

# Number of Blue Balls per node: blue (5 balls for now)
# Number of Red Balls per node: red (5 balls for now)

# Movement Record Dictionary: M = {}

# Output:
# M = {ball_ID: [node_ID, node_ID, ...], ball_ID: [node_ID, node_ID, ...], ...}


# Algorithm:
# 1. Initialize M = {}
# 2. Assign each node in V input amount of blue and red balls
# 3. Randomize then fix the order nodes in V to traverse
# 4. Randomly select a starting current_node in V
# 5. Record the current_node in M for each ball
# 6. Randomly select a neighbor_node of current_node in V
# 7. Record the neighbor_node in M for each ball
# 8. Apply the following rules of transactions between balls of current_node and neighbor_node:
#    a. [insert rule]
#    b. [insert rule]
#    c. [insert rule]
#    d. [insert rule]
# 9. Assign current_node as neighbor_node
# 10. Repeat steps 5-9 until n iterations
# 11. Return M


def main():
    pass


if __name__ == "__main__":
    main()
