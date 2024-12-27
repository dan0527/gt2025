def path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    # Base case: if start equals end, path exists
    if start == end:
        return True
    
    # Mark the node as visited
    visited.add(start)
    
    # Check all neighbors of the current node
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if path_exists(graph, neighbor, end, visited):
                return True
    
    return False

# Representing the graph from the image as an adjacency list
graph = {
    1: [2],
    2: [1, 5],
    5: [2],
    3: [6],
    6: [3, 4, 7],
    4: [6, 7],
    7: [6, 4]
}

# Asking user for input
start_node = int(input("Enter the starting node: "))
end_node = int(input("Enter the ending node: "))

# Checking path existence
if path_exists(graph, start_node, end_node):
    print("True: A path exists between the nodes.")
else:
    print("False: No path exists between the nodes.")