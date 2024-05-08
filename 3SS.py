def bfs_shortest_path(graph, start):
    queue = [start]  # Queue to store vertices to visit
    distances = {start: 0}  # Dictionary to store the distances from the start vertex

    while queue:
        vertex = queue.pop(0)

        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances


graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i + 1)
    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")

    # Add vertices to the graph if they don't exist
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    graph[src].append(dest)
    graph[dest].append(src)

start_vertex = input("Enter the start vertex: ")

shortest_distances = bfs_shortest_path(graph, start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)


























#
# This code implements a breadth-first search (BFS) algorithm to find the shortest path from a given start vertex to all other vertices in an undirected graph. Here's how it works:
#
# 1. **BFS Shortest Path Function (`bfs_shortest_path`):**
#    - It takes two parameters: `graph`, representing the undirected graph as an adjacency list, and `start`, representing the starting vertex for BFS.
#    - It uses a queue (`queue`) to store vertices to visit and a dictionary (`distances`) to store the shortest distances from the start vertex.
#    - It starts by initializing the queue with the start vertex and setting its distance to 0 in the `distances` dictionary.
#    - While the queue is not empty, it dequeues a vertex (`vertex`) from the queue.
#    - For each neighbor (`neighbor`) of the dequeued vertex, if the neighbor is not already in `distances`, it calculates its distance from the start vertex as the distance of the dequeued vertex plus one (since all edges have a weight of 1 in an unweighted graph). It then adds the neighbor to the queue.
#
# 2. **Input and Output Handling:**
#    - The code first asks the user to input the number of edges in the graph (`num_edges`).
#    - It then prompts the user to input the start and end vertices for each edge, constructing the undirected graph using an adjacency list representation.
#    - After constructing the graph, it asks the user to input the start vertex (`start_vertex`) for finding the shortest distances using BFS.
#    - Finally, it calls the `bfs_shortest_path` function and prints the shortest distances from the start vertex to all other vertices in the graph.
#
# Here's an example of how you can use this code:
#
# ```
# Enter the number of edges: 4
#
# For Edge 1
# Enter start vertex: A
# Enter end vertex: B
#
# For Edge 2
# Enter start vertex: B
# Enter end vertex: C
#
# For Edge 3
# Enter start vertex: C
# Enter end vertex: D
#
# For Edge 4
# Enter start vertex: D
# Enter end vertex: A
#
# Enter the start vertex: A
# Shortest distances from vertex A
# A : 0
# B : 1
# D : 1
# C : 2
# ```
#
# In this example, we have a graph with edges A-B, B-C, C-D, and D-A. The shortest distances from vertex A to all other vertices are printed as the output.
