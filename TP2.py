from collections import defaultdict

class GraphComponents:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.num_vertices = len(adjacency_matrix)

    def convert_to_adjacency_lists(self, undirected=False):
        """Generate adjacency lists from the matrix; optionally treat as undirected"""
        adjacency_list = defaultdict(list)
        for src in range(self.num_vertices):
            for dest in range(self.num_vertices):
                if self.adjacency_matrix[src][dest]:
                    adjacency_list[src].append(dest)
                    if undirected:
                        adjacency_list[dest].append(src)
        return adjacency_list

    def depth_first_search(self, vertex, visited, adjacency_list):
        """Recursive depth-first search"""
        visited[vertex] = True
        for neighbor in adjacency_list[vertex]:
            if not visited[neighbor]:
                self.depth_first_search(neighbor, visited, adjacency_list)

    def transpose_graph(self):
        """Create the transpose of the graph"""
        transposed = defaultdict(list)
        for src in range(self.num_vertices):
            for dest in range(self.num_vertices):
                if self.adjacency_matrix[src][dest]:
                    transposed[dest].append(src)
        return transposed

    def fill_vertex_stack(self, vertex, visited, stack, adjacency_list):
        """Order vertices in decreasing finish time for Kosaraju's algorithm"""
        visited[vertex] = True
        for neighbor in adjacency_list[vertex]:
            if not visited[neighbor]:
                self.fill_vertex_stack(neighbor, visited, stack, adjacency_list)
        stack.append(vertex)

    def count_weakly_connected_components(self):
        """Calculate the number of weakly connected components"""
        visited = [False] * self.num_vertices
        component_count = 0
        adjacency_list = self.convert_to_adjacency_lists(undirected=True)

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.depth_first_search(vertex, visited, adjacency_list)
                component_count += 1

        return component_count

    def count_strongly_connected_components(self):
        """Calculate the number of strongly connected components using Kosaraju's algorithm"""
        stack = []
        visited = [False] * self.num_vertices
        adjacency_list = self.convert_to_adjacency_lists()

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.fill_vertex_stack(vertex, visited, stack, adjacency_list)

        transposed_adjacency_list = self.transpose_graph()
        visited = [False] * self.num_vertices
        component_count = 0

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                self.depth_first_search(vertex, visited, transposed_adjacency_list)
                component_count += 1

        return component_count

if __name__ == "__main__":
    adjacency_matrix = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    graph = GraphComponents(adjacency_matrix)
    num_weakly_connected = graph.count_weakly_connected_components()
    num_strongly_connected = graph.count_strongly_connected_components()

    print(f"Number of weakly connected components: {num_weakly_connected}")
    print(f"Number of strongly connected components: {num_strongly_connected}")
