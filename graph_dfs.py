my_graph = {
    'A': {'C', 'D'},
    'B': {'H', 'G'},
    'C': {'A', 'F'},
    'D': {'A', 'E'},
    'E': {'D', 'F', 'H'},
    'F': {'C', 'E', 'G'},
    'G': {'B', 'F', 'H'},
    'H': {'B', 'E', 'G'}}


def graph_dfs(graph, curr_vertex, used):
    used.add(curr_vertex)
    for neigh_vertex in graph[curr_vertex]:
        if neigh_vertex not in used:
            graph_dfs(graph, neigh_vertex, used)


used = set()
# N - number of linked components
N = 0
for vertex in my_graph:
    if vertex not in used:
        graph_dfs(my_graph, vertex, used)
        N += 1
print(N)