def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return

    next_queue = []
    for vertex in queue:
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            next_queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    bfs_recursive(graph, next_queue, visited)


# Accepting the graph from the user
graph = {}
vertices = int(input("Enter the number of vertices: "))

for i in range(vertices):
    vertex = input("Enter a vertex: ")
    adjacent_vertices = input("Enter adjacent vertices (space-separated): ").split()
    graph[vertex] = adjacent_vertices

start_vertex = input("Enter the start vertex: ")

# Performing DFS traversal
print("DFS Traversal:")
dfs_recursive(graph, start_vertex)
print()

# Performing BFS traversal
print("BFS Traversal:")
bfs_recursive(graph, [start_vertex])
print()































# This code defines two graph traversal functions, `dfs_recursive` for Depth-First Search (DFS) and `bfs_recursive` for Breadth-First Search (BFS), both implemented recursively. Here's an explanation of the code flow and the theory behind DFS and BFS:
#
# 1. **Depth-First Search (DFS) Recursive Function (`dfs_recursive`):**
#    - DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking.
#    - The `dfs_recursive` function recursively visits vertices starting from the given `start` vertex.
#    - It maintains a set `visited` to track visited vertices and ensures that each vertex is visited only once.
#    - The function prints each visited vertex and recursively explores its unvisited neighbors.
#    - This implementation assumes that the graph is represented as an adjacency list (`graph`), where each vertex maps to a list of its adjacent vertices.
#
# 2. **Breadth-First Search (BFS) Recursive Function (`bfs_recursive`):**
#    - BFS is another graph traversal algorithm that explores all vertices at the current depth before moving to the next level.
#    - The `bfs_recursive` function recursively visits vertices in a level-by-level manner starting from the given `start` vertex.
#    - It maintains a set `visited` to track visited vertices and ensures that each vertex is visited only once.
#    - The function uses a queue (`queue`) to process vertices at each level and explores their unvisited neighbors.
#    - This implementation assumes that the graph is represented as an adjacency list (`graph`), where each vertex maps to a list of its adjacent vertices.
#
# **Flow of the Code:**
# 1. The code accepts input for the number of vertices and the adjacency list representation of the graph.
# 2. It then asks for the start vertex for both DFS and BFS traversal.
# 3. The `dfs_recursive` function performs a recursive DFS traversal starting from the specified start vertex.
# 4. The `bfs_recursive` function performs a recursive BFS traversal starting from the specified start vertex using a queue.
# 5. The main part of the code prints the DFS and BFS traversals.
#
# Both DFS and BFS traversal algorithms are essential in graph theory and have various applications, such as finding paths, cycles, connected components, and more.
#
#
# Here's a sample execution of the provided code with a sample input containing 5 vertices:
#
# **Sample Input:**
# ```
# Enter the number of vertices: 5
#
# Enter a vertex: A
# Enter adjacent vertices (space-separated): B C
# Enter a vertex: B
# Enter adjacent vertices (space-separated): A C D
# Enter a vertex: C
# Enter adjacent vertices (space-separated): A B D E
# Enter a vertex: D
# Enter adjacent vertices (space-separated): B C E
# Enter a vertex: E
# Enter adjacent vertices (space-separated): C D
# Enter the start vertex: A
# ```
#
# **Expected Output:**
# ```
# DFS Traversal:
# A B C D E
#
# BFS Traversal:
# A B C D E
# ```
#
# Explanation:
# - The input defines a graph with 5 vertices (A, B, C, D, E) and their respective adjacent vertices.
# - The DFS traversal starting from vertex A visits vertices in the order A, B, C, D, E.
# - The BFS traversal starting from vertex A also visits vertices in the order A, B, C, D, E, following a level-by-level approach.
#
#
#
