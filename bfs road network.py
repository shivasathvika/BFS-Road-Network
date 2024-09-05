from collections import deque

# Define graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Define BFS algorithm to find shortest path
def bfs_shortest_path(graph, start, goal):
    visited = {start}
    queue = deque([(start, [])])
    while queue:
        (current_node, path) = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor == goal:
                    return path + [(current_node, neighbor)]
                else:
                    queue.append((neighbor, path + [(current_node, neighbor)]))

# Test with sample graph
start_node = 'A'
end_node = 'F'
shortest_path = bfs_shortest_path(graph, start_node, end_node)

# Print results
if shortest_path is None:
    print(f"No path found between {start_node} and {end_node}")
else:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")

