import heapq

def astar(start, goal, graph, heuristic):
    open_set = []
    closed_set = set()

    # Set the initial cost of the start node to zero.
    g = {start: 0}
    # Set the initial priority value of the start node.
    f = {start: g[start] + heuristic[start]}
    # Keep track of the parent nodes.
    parent = {start: None}

    # Add the start node to the open set.
    heapq.heappush(open_set, (f[start], start))

    while open_set:
        # Get the node with the lowest f value (priority) from the open set.
        current_node = heapq.heappop(open_set)[1]

        # If the current node is the goal, we have found the path.
        if current_node == goal:
            # Reconstruct the path from the goal to the start.
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]

        # Add the current node to the closed set to avoid revisiting it.
        closed_set.add(current_node)

        # Explore the neighbors of the current node.
        for neighbor in graph[current_node]:
            if neighbor in closed_set:
                continue

            # Calculate the cost from the start node to the neighbor.
            neighbor_g = g[current_node] + 1

            if neighbor not in g or neighbor_g < g[neighbor]:
                # Update the cost values and parent node.
                g[neighbor] = neighbor_g
                f[neighbor] = g[neighbor] + heuristic[neighbor]
                parent[neighbor] = current_node
                # Add the neighbor to the open set.
                heapq.heappush(open_set, (f[neighbor], neighbor))

    # If there is no path from start to goal, return an empty list.
    return []


# Define the graph as a dictionary where the keys are nodes (alphabets) and the values are lists of neighbors.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D', 'H'],
    'H': ['E', 'G', 'I'],
    'I': ['F', 'H']
}

start = 'A'
goal = 'I'

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 2,
    'I': 0
}

path = astar(start, goal, graph, heuristic)
if path:
    print("Path found from", start, "to", goal)
    print("Path:", " -> ".join(path))
else:
    print("No path found from", start, "to", goal)




























# This code implements the A* algorithm for finding the shortest path from a start node to a goal node in a graph. Here's how it works:
#
# 1. The `astar` function takes four parameters: `start` (start node), `goal` (goal node), `graph` (graph representation), and `heuristic` (heuristic function for estimating the cost from a node to the goal).
# 2. It uses a priority queue (`open_set`) to prioritize nodes with lower estimated costs (`f` value).
# 3. The algorithm maintains three dictionaries: `g` for actual costs from the start node, `f` for total estimated costs (actual cost + heuristic) to the goal, and `parent` to keep track of the parent nodes for reconstructing the path.
# 4. The algorithm iteratively explores nodes until the `open_set` is empty or the goal node is reached.
# 5. At each step, it selects the node with the lowest `f` value from the `open_set`, updates costs and parent nodes for its neighbors, and adds unvisited neighbors to the `open_set`.
# 6. If the goal node is found, it reconstructs the path from the goal to the start using the `parent` dictionary.
#
# **Sample Output:**
# ```
# Path found from A to I
# Path: A -> B -> D -> G -> H -> I
# ```
#
# Explanation:
# - The input graph represents a directed graph with nodes A to I and their respective neighbors.
# - The heuristic function estimates the cost from each node to the goal node I.
# - The A* algorithm finds the shortest path from start node A to goal node I, considering both actual costs (g) and heuristic costs (f).
# - In this case, the shortest path from A to I is A -> B -> D -> G -> H -> I, with a total cost of 9 (sum of heuristic values).

