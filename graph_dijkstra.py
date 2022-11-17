from collections import deque

my_graph = {
    'A': {'C': 3, 'D': 2},
    'B': {'H': 5, 'G': 2},
    'C': {'A': 3, 'F': 6},
    'D': {'A': 2, 'E': 1},
    'E': {'D': 1, 'F': 3, 'H': 6},
    'F': {'C': 6, 'E': 3, 'G': 2},
    'G': {'B': 2, 'F': 2, 'H': 4},
    'H': {'B': 5, 'E': 6, 'G': 4}
}


def dijkstra(graph, start_vertex, end_vertex):
    if start_vertex not in graph or end_vertex not in graph:
        return print(f'Какой-то из вершин нет в графе, проверьте ввод!')
    queue = deque([start_vertex])
    short_distances = {}
    short_distances[start_vertex] = 0
    while queue:
        curr_v = queue.popleft()
        for neigh_v in graph[curr_v]:
            if neigh_v not in short_distances or short_distances[curr_v] + graph[curr_v][neigh_v] < short_distances[neigh_v]:
                short_distances[neigh_v] = short_distances[curr_v] + graph[curr_v][neigh_v]
                queue.append(neigh_v)
    return print(short_distances)


dijkstra(my_graph, 'D', 'H')
