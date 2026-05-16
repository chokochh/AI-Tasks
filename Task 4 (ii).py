# Depth First Search (DFS)
# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS Function
def dfs(graph, start, goal, path=None, visited=None):

    # Initialize path and visited set
    if path is None:
        path = []

    if visited is None:
        visited = set()

    # Add current node
    path.append(start)
    visited.add(start)

    # Goal test
    if start == goal:
        return path

    # Explore neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited.copy())

            if result is not None:
                return result

    return None

# Main Program
start_node = 'A'
goal_node = 'F'

path = dfs(graph, start_node, goal_node)

print("DFS Search Path:")
print(" -> ".join(path))
