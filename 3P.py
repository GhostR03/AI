def prims_algorithm(graph, start_vertex):
    visited = {start_vertex}
    minimum_spanning_tree = []
    edges = []

    while len(visited) < len(graph):
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    edges.append((weight, vertex, neighbor))

        weight, src, dest = min(edges)
        edges.remove((weight, src, dest))

        if dest not in visited:
            visited.add(dest)
            minimum_spanning_tree.append((src, dest, weight))

    return minimum_spanning_tree


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

start_vertex = input("Enter the starting vertex for finding Minimum Spanning Tree: ")

minimum_spanning_tree = prims_algorithm(graph, start_vertex)

total_cost = 0
for src, dest, weight in minimum_spanning_tree:
    total_cost += weight

print("\nMinimum Spanning Tree:")
for src, dest, weight in minimum_spanning_tree:
    print(src, "-->", dest, ": ", weight)

print("Total Cost:", total_cost)



































#
# Your code implements Prim's algorithm for finding the Minimum Spanning Tree (MST) of a graph. Here's how it works:
#
# 1. **Input Graph:**
#    - The user inputs the number of edges in the graph.
#    - For each edge, they provide the start vertex, end vertex, and weight.
#
# 2. **Prims's Algorithm:**
#    - The algorithm starts with a set of visited vertices containing only the start vertex.
#    - It initializes an empty list for the minimum spanning tree (`minimum_spanning_tree`) and a list for potential edges to consider (`edges`).
#    - While the number of visited vertices is less than the total vertices in the graph:
#      - For each visited vertex, it looks at its neighbors and adds their edges to the `edges` list if the neighbor is not already visited.
#      - It then selects the minimum weight edge from `edges` and removes it.
#      - If the destination vertex of this edge is not visited, it adds it to the visited set and includes this edge in the minimum spanning tree.
#    - This process continues until all vertices are visited.
#
# 3. **Output:**
#    - The algorithm outputs the minimum spanning tree (`minimum_spanning_tree`) and calculates the total cost by summing up the weights of edges in the MST.
#
# This code efficiently finds the Minimum Spanning Tree using Prim's algorithm, ensuring that the tree spans all vertices with minimal total weight.
#
#
# Here are sample inputs you can use to test the Prim's algorithm code:
#
# ```
# Enter the number of edges: 6
#
# For Edge 1
# Enter start vertex: A
# Enter end vertex: B
# Enter weight: 2
#
# For Edge 2
# Enter start vertex: A
# Enter end vertex: C
# Enter weight: 3
#
# For Edge 3
# Enter start vertex: B
# Enter end vertex: C
# Enter weight: 1
#
# For Edge 4
# Enter start vertex: B
# Enter end vertex: D
# Enter weight: 4
#
# For Edge 5
# Enter start vertex: C
# Enter end vertex: D
# Enter weight: 5
#
# For Edge 6
# Enter start vertex: D
# Enter end vertex: E
# Enter weight: 6
#
# Enter the starting vertex for finding Minimum Spanning Tree: A
# ```
#
# These inputs define a graph with five vertices (A, B, C, D, E) and six edges with corresponding weights. The starting vertex for finding the Minimum Spanning Tree is set to A. You can modify these inputs or add more edges/vertices as needed to test different scenarios.