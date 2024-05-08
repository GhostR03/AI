def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskals_algorithm(graph):
    minimum_spanning_tree = []
    edges = []

    for src in graph:
        for dest, weight in graph[src]:
            edges.append((weight, src, dest))

    edges.sort()

    parent = {}
    rank = {}

    for vertex in graph:
        parent[vertex] = vertex
        rank[vertex] = 0

    for edge in edges:
        weight, src, dest = edge

        src_root = find(parent, src)
        dest_root = find(parent, dest)

        if src_root != dest_root:
            minimum_spanning_tree.append((src, dest, weight))
            union(parent, rank, src_root, dest_root)

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

minimum_spanning_tree = kruskals_algorithm(graph)

total_cost = 0
for src, dest, weight in minimum_spanning_tree:
    total_cost += weight

print("\nMinimum Spanning Tree:")
for src, dest, weight in minimum_spanning_tree:
    print(src, "-->", dest, ": ", weight)

print("Total Cost:", total_cost)





# This code implements Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of a graph. Here's an overview of how it works:
#
# 1. **`find(parent, i)` Function**: This function finds the parent of a vertex `i` in the union-find data structure. It uses recursion to find the ultimate parent (root) of the set containing `i`.
#
# 2. **`union(parent, rank, x, y)` Function**: This function performs the union operation of two sets represented by their respective root nodes `x` and `y`. It uses the rank heuristic to optimize the union by attaching the smaller tree to the root of the larger tree.
#
# 3. **`kruskals_algorithm(graph)` Function**: This is the main function that implements Kruskal's algorithm. It takes a graph as input, where each vertex is associated with its neighboring vertices and edge weights. The algorithm follows these steps:
#    - It initializes an empty list `minimum_spanning_tree` to store the edges of the MST.
#    - It creates a list `edges` containing all edges sorted by their weights in ascending order.
#    - It initializes the union-find data structures `parent` and `rank` for each vertex in the graph.
#    - It iterates through the sorted edges and adds them to the MST if adding the edge does not form a cycle (checked using the union-find operations).
#    - Finally, it returns the `minimum_spanning_tree`, which represents the MST.
#
# 4. **Input Processing**: The code takes input from the user to build the graph. It asks for the number of edges and then iteratively asks for the start vertex, end vertex, and weight of each edge.
#
# 5. **Output**: After running Kruskal's algorithm, the code prints the edges of the MST along with their weights and calculates the total cost of the MST.
#
# To test the code, you can input a graph with edges and weights and observe the generated Minimum Spanning Tree and its total cost.
#
# Sure, here are some sample inputs you can use to test the Kruskal's algorithm implementation:
#
# **Input 1:**
# ```
# Enter the number of edges: 6
#
# For Edge 1
# Enter start vertex: A
# Enter end vertex: B
# Enter weight: 5
#
# For Edge 2
# Enter start vertex: B
# Enter end vertex: C
# Enter weight: 4
#
# For Edge 3
# Enter start vertex: C
# Enter end vertex: D
# Enter weight: 2
#
# For Edge 4
# Enter start vertex: D
# Enter end vertex: A
# Enter weight: 1
#
# For Edge 5
# Enter start vertex: A
# Enter end vertex: C
# Enter weight: 3
#
# For Edge 6
# Enter start vertex: B
# Enter end vertex: D
# Enter weight: 2
# ```
#
# **Input 2:**
# ```
# Enter the number of edges: 5
#
# For Edge 1
# Enter start vertex: 1
# Enter end vertex: 2
# Enter weight: 4
#
# For Edge 2
# Enter start vertex: 2
# Enter end vertex: 3
# Enter weight: 5
#
# For Edge 3
# Enter start vertex: 3
# Enter end vertex: 4
# Enter weight: 2
#
# For Edge 4
# Enter start vertex: 4
# Enter end vertex: 1
# Enter weight: 1
#
# For Edge 5
# Enter start vertex: 1
# Enter end vertex: 3
# Enter weight: 3
# ```
#
# These inputs create two different graphs with edges and weights. You can run the Kruskal's algorithm code with these inputs to see the Minimum Spanning Tree and its total cost.
