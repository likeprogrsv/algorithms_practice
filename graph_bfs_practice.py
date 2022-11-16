from collections import deque

my_graph = {
    'A': {'C', 'D'},
    'B': {'H', 'G'},
    'C': {'A', 'F'},
    'D': {'A', 'E'},
    'E': {'D', 'F', 'H'},
    'F': {'C', 'E', 'G'},
    'G': {'B', 'F', 'H'},
    'H': {'B', 'E', 'G'}
}
parents = {v: None for v in my_graph}


def bfs(graph, start_vertex):
    if start_vertex not in graph:
        return print(f'Vertex {start_vertex} does not exist')

    queue = deque([start_vertex])
    distances = {v: None for v in graph}
    distances[start_vertex] = 0

    while queue:
        curr_v = queue.popleft()
        for neigh_v in graph[curr_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[curr_v] + 1
                parents[neigh_v] = curr_v
                queue.append(neigh_v)
    print(distances)


def find_path(graph, end_vertex):
    if end_vertex not in graph:
        return print(f'Vertex {end_vertex} does not exist')
    path = [end_vertex]
    parent = end_vertex
    while parents[parent] is not None:
        parent = parents[parent]
        path.append(parent)

    return print(path[::-1])


bfs(my_graph, 'G')
find_path(my_graph, 'A')
