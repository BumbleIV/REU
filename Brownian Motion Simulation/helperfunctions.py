def node_most_balls(M: dict) -> tuple:
    map = {}

    for ball_ID in M:
        last_node = M[ball_ID][-1]

        if last_node in map:
            map[last_node] += 1
        else:
            map[last_node] = 1

    node = max(map, key=map.get)
    return node, map[node]


def node_most_balls_2(G) -> tuple:
    max_balls = 0
    max_node = None

    for i in G:
        if len(G.nodes[i]['Balls']) > max_balls:
            max_balls = len(G.nodes[i]['Balls'])
            max_node = i

    return (max_node, max_balls)
