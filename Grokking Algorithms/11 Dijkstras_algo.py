def dijkstra_algo(graph, start):
    current_node = start
    checked = []
    length = {v: float('inf') for v in graph}
    length[start] = 0
    parents = {}

    while True:
        for node in graph[current_node]:
            if node[1] + length[current_node] < length[node[0]]:
                parents[node[0]] = current_node
                length[node[0]] = length[current_node] + node[1]

        checked.append(current_node)
        if len(checked) == len(graph): break
        current_node = min([i for i in length if i not in checked], key=lambda x: length[x])

    return length, parents


def find_path(start, end, par):
    path = []
    curr = end
    path.append(end)
    while True:
        path.append(par[curr])
        curr = par[curr]
        if par[curr] == start:
            path.append(start)
            break
    return path[::-1]


graph = {
    'start': [['A', 5], ['B', 2]],
    'A': [['C', 7], ['D', 2]],
    'B': [['A', 8], ['D', 7]],
    'C': [['end', 2], ['D', 6]],
    'D': [['end', 1]],
    'end': []
}


results = dijkstra_algo(graph, 'start')

print(*results, find_path('start', 'end', results[1]), sep='\n')
