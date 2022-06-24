# prints map
def print_map(M: dict) -> None:
    for key, value in M.items():
        print("{}: {}".format(key, value) + "\n")


# returns node with most balls in map as tuple
def max_balls_map(M: dict) -> tuple:
    map = {}

    for ball_ID in M:
        last_node = M[ball_ID][-1]

        if last_node in map:
            map[last_node] += 1
        else:
            map[last_node] = 1

    node = max(map, key=map.get)
    return (node, map[node])


# returns node with most balls in graph as tuple
def max_balls_graph(G) -> tuple:
    max_balls = 0
    max_node = None

    for i in G:
        if len(G.nodes[i]['Balls']) > max_balls:
            max_balls = len(G.nodes[i]['Balls'])
            max_node = i

    return (max_node, max_balls)
