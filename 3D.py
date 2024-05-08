def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # List to store visited vertices
    visited = []

    while len(visited) < len(graph):
        # Find the vertex with the minimum distance
        min_distance = float('inf')
        min_vertex = None

        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            # There is no path to the remaining unvisited vertices
            break

        # Add the vertex to the visited list
        visited.append(min_vertex)

        # Update the distances of its neighbors
        for neighbor, weight in graph[min_vertex]:
            distance = distances[min_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


# Accept graph input from the user
graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i + 1)

    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")
    weight = int(input("Enter weight: "))

    # Add the edge to the graph
    if src in graph:
        graph[src].append((dest, weight))
    else:
        graph[src] = [(dest, weight)]

    if dest in graph:
        graph[dest].append((src, weight))
    else:
        graph[dest] = [(src, weight)]

start_vertex = input("Enter the starting vertex: ")

# Apply Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_vertex)

print("\nShortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print("Vertex:", vertex, "Distance:", distance)

# Dijkstra's algorithm is a graph traversal algorithm used to find the shortest path from a starting vertex to all other vertices in a weighted graph. It works by iteratively exploring the vertices and updating their distances from the starting vertex.
#
# Here's how the Dijkstra's algorithm works:
#
# 1. **Initialization:**
#    - Create a dictionary `distances` to store the shortest distances from the starting vertex to each vertex in the graph. Initialize all distances to infinity except for the starting vertex, which is set to 0.
#    - Create an empty list `visited` to keep track of visited vertices.
#
# 2. **Main Loop:**
#    - While the number of visited vertices is less than the total number of vertices in the graph:
#      - Find the vertex with the minimum distance among the unvisited vertices. This is the vertex that will be explored next.
#      - Add this vertex to the `visited` list.
#      - Update the distances of its unvisited neighbors by considering the edge weights. If the newly calculated distance is shorter than the current distance stored in `distances`, update the distance.
#
# 3. **Termination:**
#    - Once all vertices have been visited or there are no reachable vertices left, the algorithm terminates.
#
# 4. **Output:**
#    - The `distances` dictionary contains the shortest distances from the starting vertex to all other vertices in the graph.
#
# **Example:**
# Let's walk through a simple example to understand Dijkstra's algorithm better.
#
# Consider the following weighted graph:
# ```
#           5      3
#      A ------- B ------- D
#      |         |       /
#      |         |     6
#      |         |   /
#      |        2  /
#      |       /  /
#      |     /   /
#      |   /    /
#      | /     /
#      C ------ E
#           2
# ```
#
# Suppose we start at vertex 'A'. The edge weights are as follows:
# - Edge (A, B): 5
# - Edge (A, C): 3
# - Edge (B, C): 2
# - Edge (B, D): 6
# - Edge (B, E): 2
# - Edge (C, E): 4
#
# 1. **Initialization:**
#    - Initialize `distances` as follows: `distances = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf}`.
#    - Initialize `visited` as an empty list.
#
# 2. **Main Loop:**
#    - Start with vertex 'A'. Since 'A' is the starting vertex, its distance is 0. Add 'A' to the `visited` list.
#    - Update the distances of 'B' and 'C' based on their edges from 'A'.
#    - Move to the next closest unvisited vertex, which is 'C' with a distance of 3. Add 'C' to the `visited` list.
#    - Update the distance of 'E' based on its edge from 'C'.
#    - Continue this process until all vertices are visited or unreachable.
#
# 3. **Output:**
#    - After the algorithm terminates, `distances` will contain the shortest distances from 'A' to all other vertices: `{'A': 0, 'B': 5, 'C': 3, 'D': 7, 'E': 5}`.
#
# Dijkstra's algorithm guarantees the shortest path from the starting vertex to any other vertex in the graph, provided that the edge weights are non-negative. It's commonly used in network routing protocols, pathfinding algorithms, and optimization problems involving graphs.
#
# Here's an example of input and expected output for the Dijkstra's algorithm implementation:
#
# **Sample Input:**
# ```
# Enter the number of edges: 6
#
# For Edge 1
# Enter start vertex: A
# Enter end vertex: B
# Enter weight: 5
#
# For Edge 2
# Enter start vertex: A
# Enter end vertex: C
# Enter weight: 3
#
# For Edge 3
# Enter start vertex: B
# Enter end vertex: C
# Enter weight: 2
#
# For Edge 4
# Enter start vertex: B
# Enter end vertex: D
# Enter weight: 6
#
# For Edge 5
# Enter start vertex: C
# Enter end vertex: D
# Enter weight: 4
#
# For Edge 6
# Enter start vertex: C
# Enter end vertex: E
# Enter weight: 2
#
# Enter the starting vertex: A
# ```
#
# **Expected Output:**
# ```
# Shortest distances from vertex A
# Vertex: A Distance: 0
# Vertex: B Distance: 5
# Vertex: C Distance: 3
# Vertex: D Distance: 7
# Vertex: E Distance: 5
# ```
#
# In this example, the user inputs a graph with 6 edges and specifies the weights of each edge. The starting vertex is set as 'A'. The program then applies Dijkstra's algorithm to find the shortest distances from vertex 'A' to all other vertices in the graph. The expected output shows the shortest distances from vertex 'A' to each vertex in the graph.
