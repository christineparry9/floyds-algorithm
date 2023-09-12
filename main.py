def floyd_warshall(graph, n=None, k=0):
    """
    A recursive version of Floyd-Warshall algorithm for all-pairs shortest path.

    :param graph: A 2D list representing the graph's adjacency matrix.
    :param n: The number of nodes in the graph.
    :param k: The current node being considered.
    :return: A 2D list representing the shortest path distances between every pair of nodes.
    """
    if n is None:
        n = len(graph)

    if k == n:
        return graph

    # Recursively compute the shortest paths
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return floyd_warshall(new_graph, n, k + 1)


if __name__ == "__main__":
    # Define a graph using an adjacency matrix
    # Use float('inf') to represent infinite distances
    graph = [
        [0, 3, float('inf'), 5],
        [2, 0, float('inf'), 4],
        [float('inf'), 1, 0, float('inf')],
        [float('inf'), float('inf'), 2, 0]
    ]

    distances = floyd_warshall(graph)
    for row in distances:
        print(row)
