from heapq import heappush, heappop

def create_weighted_graph():
    """
    Creates a weighted, undirected graph represented as an adjacency matrix.
    Returns:
        matrix: 2D list representing the graph.
    """
    # Number of vertices
    size = 9  
    matrix = [[0] * size for _ in range(size)]  # Initialize adjacency matrix
    
    # List of edges
    edges = [
        (1, 2, 4), (1, 5, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 7, 2), (6, 4, 5),
        (7, 8, 8), (7, 9, 2),
        (8, 9, 1)
    ]
    
    for u, v, weight in edges:
        matrix[u - 1][v - 1] = weight  
        matrix[v - 1][u - 1] = weight 
        
    return matrix

def prims_algorithm(graph, start):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST).
    
    Args:
        graph: 2D list representing the adjacency matrix of the graph.
        start: Starting node (1-based index).
    
    Returns:
        mst_edges: List of edges in the MST.
        total_weight: Total weight of the MST.
    """
    num_vertices = len(graph)
    visited = [False] * num_vertices
    mst_edges = []
    total_weight = 0
    
    priority_queue = [(0, start - 1, None)] 
    
    while priority_queue:
        weight, current, parent = heappop(priority_queue)
        
        if visited[current]:
            continue
        
        visited[current] = True
        
        if parent is not None:
            mst_edges.append((parent + 1, current + 1, weight))
            total_weight += weight
        
        for neighbor in range(num_vertices):
            if graph[current][neighbor] > 0 and not visited[neighbor]:
                heappush(priority_queue, (graph[current][neighbor], neighbor, current))
    
    return mst_edges, total_weight

def find_set(parent, node):
    """
    Finds the representative of the set containing 'node' using path compression.
    """
    if parent[node] != node:
        parent[node] = find_set(parent, parent[node])
    return parent[node]

def union_sets(parent, rank, node1, node2):
    """
    Merges two sets containing 'node1' and 'node2' using rank-based union.
    """
    root1 = find_set(parent, node1)
    root2 = find_set(parent, node2)
    
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskals_algorithm(graph):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST).
    
    Args:
        graph: 2D list representing the adjacency matrix of the graph.
    
    Returns:
        mst_edges: List of edges in the MST.
        total_weight: Total weight of the MST.
    """
    num_vertices = len(graph)
    edges = []
    
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices): 
            if graph[i][j] > 0:
                edges.append((graph[i][j], i, j))
    
    edges.sort()
    
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in edges:
        if find_set(parent, u) != find_set(parent, v):
            union_sets(parent, rank, u, v)
            mst_edges.append((u + 1, v + 1, weight)) 
            total_weight += weight
    
    return mst_edges, total_weight

graph = create_weighted_graph()
root_node = int(input("Enter the root node (1-9): "))

# Run Prim's algorithm
print("\nResults of Prim's Algorithm:")
prims_result, prims_total = prims_algorithm(graph, root_node)
print("MST Edges:", prims_result)
print("Total Weight of MST:", prims_total)

# Run Kruskal's algorithm
print("\nResults of Kruskal's Algorithm:")
kruskals_result, kruskals_total = kruskals_algorithm(graph)
print("MST Edges:", kruskals_result)
print("Total Weight of MST:", kruskals_total)
