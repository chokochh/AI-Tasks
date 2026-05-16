# Breadth First Search (BFS)
# BFS explores nodes level by level using a Queue
from collections import deque
# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Function
def bfs(graph, start, goal):
    queue = deque([[start]])  # Queue stores paths
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        # Goal test
        if node == goal:
            return path

        # Visit node if not already visited
        if node not in visited:
            visited.add(node)

            # Expand neighbors
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# Main Program
start_node = 'A'
goal_node = 'F'

path = bfs(graph, start_node, goal_node)

print("BFS Search Path:")
print(" -> ".join(path))
