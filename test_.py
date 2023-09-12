import unittest

def floyd_warshall(graph, n=None, k=0):
    if n is None:
        n = len(graph)
    if k == n:
        return graph
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return floyd_warshall(new_graph, n, k + 1)

class TestFloydWarshall(unittest.TestCase):

    def test_single_node_graph(self):
        graph = [[0]]
        result = floyd_warshall(graph)
        self.assertEqual(result, [[0]])

    def test_two_node_graph(self):
        graph = [
            [0, 3],
            [2, 0]
        ]
        result = floyd_warshall(graph)
        self.assertEqual(result, [[0, 3], [2, 0]])

    def test_four_node_graph(self):
        graph = [
            [0, 3, float('inf'), 5],
            [2, 0, float('inf'), 4],
            [float('inf'), 1, 0, float('inf')],
            [float('inf'), float('inf'), 2, 0]
        ]
        result = floyd_warshall(graph)
        expected_result = [
            [0, 3, 7, 5],
            [2, 0, 6, 4],
            [3, 1, 0, 5],
            [5, 3, 2, 0]
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
