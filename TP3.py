def create_adjacency_matrix(edges, num_nodes):
    """Create an adjacency matrix from a list of edges."""
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1  # Convert to 0-based indexing
    return matrix

def get_children(adjacency_matrix, node):
    """Retrieve the children of a given node from the adjacency matrix."""
    children = []
    for i in range(len(adjacency_matrix)):
        if adjacency_matrix[node - 1][i] == 1:  # Convert to 0-based indexing
            children.append(i + 1)
    return children

def inorder_subtree(adjacency_matrix, root):
    """Perform an inorder traversal of the subtree rooted at the given node."""
    def traverse(node, visited):
        if node in visited:
            return []
        
        visited.add(node)
        result = []
        children = get_children(adjacency_matrix, node)
        
        if children:
            result.extend(traverse(children[0], visited))  # Visit the leftmost child
        result.append(node)  # Visit the root
        if len(children) > 1:
            for child in children[1:]:  # Visit all other children
                result.extend(traverse(child, visited))
        
        return result
    
    return traverse(root, set())

if __name__ == "__main__":
    # Define the graph using edges
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
    num_nodes = 8
    adjacency_matrix = create_adjacency_matrix(edges, num_nodes)

    # Get the root node for the traversal
    root = int(input("Enter node label (1-8): "))
    if 1 <= root <= num_nodes:
        traversal_result = inorder_subtree(adjacency_matrix, root)
        print(f"Inorder traversal of subtree rooted at node {root}:", traversal_result)
    else:
        print("Invalid node label. Please enter a value between 1 and 8.")
