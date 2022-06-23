import main as m


def node_most_balls(M: dict) -> tuple:
    map = {}

    for ball_ID in M:
        last_node = M[ball_ID][-1]

        if last_node in map:
            map[last_node] += 1
        else:
            map[last_node] = 1

    return (max(map, key=map.get), map[max(map, key=map.get)])

