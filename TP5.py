import numpy as np

def build_adjacency_matrix(edges, vertices=None):
    """Generates an adjacency matrix from a list of edges."""
    if not vertices:
        vertices = sorted(set([vertex for edge in edges for vertex in edge[:2]]))
    
    vertex_index_map = {vertex: idx for idx, vertex in enumerate(vertices)}
    
    size = len(vertices)
    matrix = np.full((size, size), float('inf'))
    
    np.fill_diagonal(matrix, 0)
    
    for start, end, weight in edges:
        i, j = vertex_index_map[start], vertex_index_map[end]
        matrix[i][j] = weight
    
    return matrix, vertices, vertex_index_map

def dijkstra_algorithm(graph, start_idx, end_idx, vertices):
    """Finds the shortest path between two vertices using Dijkstra's algorithm."""
    num_vertices = len(vertices)
    distances = [float('inf')] * num_vertices
    previous_nodes = [None] * num_vertices
    visited = [False] * num_vertices
    
    distances[start_idx] = 0
    
    for _ in range(num_vertices):
        min_distance = float('inf')
        min_vertex = -1
        
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v
        
        if min_vertex == -1:  
            break
        
        visited[min_vertex] = True
        
        for v in range(num_vertices):
            if (not visited[v] and graph[min_vertex][v] != float('inf') and
                distances[min_vertex] + graph[min_vertex][v] < distances[v]):
                distances[v] = distances[min_vertex] + graph[min_vertex][v]
                previous_nodes[v] = min_vertex
    
    path = []
    current = end_idx
    
    while current is not None:
        path.append(vertices[current])
        current = previous_nodes[current]
    
    path.reverse()
    
    return path, distances[end_idx]

def main():
    # Define the graph
    edges = [
        ('A', 'C', 1), ('A', 'B', 4), ('C', 'F', 7), ('B', 'F', 3),
        ('C', 'D', 8), ('D', 'H', 5), ('F', 'H', 1), ('F', 'E', 1),
        ('E', 'H', 2), ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
        ('G', 'L', 4), ('E', 'L', 2), ('G', 'M', 4), ('L', 'M', 1)
    ]
    
    vertices = sorted(set([vertex for edge in edges for vertex in edge[:2]]))
    
    matrix, vertices, vertex_index_map = build_adjacency_matrix(edges, vertices)
    
    source = input("Enter the source vertex: ")
    target = input("Enter the target vertex: ")
    
    if source not in vertices or target not in vertices:
        print("Invalid vertices entered.")
        return
    
    path, total_cost = dijkstra_algorithm(
        matrix,
        vertex_index_map[source],
        vertex_index_map[target],
        vertices
    )
    print(f"\nThe Shortest path from {source} to {target}:")
    print(" -> ".join(path))
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    main()
