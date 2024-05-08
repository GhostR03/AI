def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # Push unvisited neighbors onto the stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs_iterative(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # Enqueue unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Accepting the graph from the user
graph = {}
vertices = int(input("Enter the number of vertices: "))

for i in range(vertices):
    vertex = input("Enter a vertex: ")
    adjacent_vertices = input("Enter adjacent vertices (space-separated): ").split()
    graph[vertex] = adjacent_vertices

start_vertex = input("Enter the start vertex: ")

# Performing iterative DFS traversal
print("DFS Traversal:")
dfs_iterative(graph, start_vertex)
print()

# Performing iterative BFS traversal
print("BFS Traversal:")
bfs_iterative(graph, start_vertex)
print()





























#
# The provided code implements Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms for traversing a graph. Here's an explanation of the flow of the code and the theory behind DFS and BFS:
#
# 1. **Depth-First Search (DFS):**
#    - DFS is an algorithm for traversing or searching tree or graph data structures.
#    - It starts at the root node (or any arbitrary node for a graph) and explores as far as possible along each branch before backtracking.
#    - The DFS algorithm uses a stack to keep track of vertices to visit next.
#    - In the iterative version (`dfs_iterative`), the algorithm maintains a set of visited vertices and a stack to process vertices. It pops a vertex from the stack, marks it as visited, prints it, and pushes its unvisited neighbors onto the stack.
#    - The DFS traversal order depends on the order of neighbors in the adjacency list. It can be used to detect cycles in a graph and explore paths deeply.
#
# 2. **Breadth-First Search (BFS):**
#    - BFS is another algorithm for traversing or searching tree or graph data structures.
#    - It starts at the root node (or any arbitrary node for a graph) and explores all of its neighbors at the current depth before moving to the next level.
#    - BFS uses a queue to keep track of vertices to visit next.
#    - In the iterative version (`bfs_iterative`), the algorithm maintains a set of visited vertices and a queue to process vertices. It dequeues a vertex from the queue, marks it as visited, prints it, and enqueues its unvisited neighbors.
#    - The BFS traversal order follows a level-by-level approach, exploring nodes at the same level before moving to the next level. It's useful for finding shortest paths in unweighted graphs and exploring neighbors broadly.
#
# **Flow of the Code:**
# 1. The code accepts input for the number of vertices and the adjacency list representation of the graph.
# 2. It then asks for the start vertex for the DFS and BFS traversal.
# 3. The `dfs_iterative` function performs an iterative DFS traversal starting from the specified start vertex.
# 4. The `bfs_iterative` function performs an iterative BFS traversal starting from the specified start vertex.
# 5. The main part of the code prints the DFS and BFS traversals.
#
# **Practical Application:**
# - DFS and BFS are fundamental graph traversal algorithms used in various applications:
#   - DFS is used in topological sorting, finding strongly connected components, solving puzzles (like maze problems), and detecting cycles in graphs.
#   - BFS is used in shortest path algorithms (when all edges have the same weight), finding connected components, and network traversal algorithms.


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
# - The DFS traversal starts from vertex A and visits vertices in the order A, B, C, D, E (or any other valid order based on the adjacency list).
# - The BFS traversal also starts from vertex A and visits vertices in the order A, B, C, D, E (or any other valid order based on the adjacency list), but with a level-by-level approach.