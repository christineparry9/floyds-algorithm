import unittest
from main import floyd_warshall
import timeit


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

    def test_large_graph(self):
        INF = float('inf')
        graph = [[0, INF, INF, INF, INF, 343, INF, 1435, 464, INF],
                [INF, 0, INF, INF, INF, 879, 954, 811, INF, 524],
                [INF, INF, 0, INF, 1364, 1054, INF, INF, INF, INF],
                [INF, INF, INF, 0, INF, INF, 433, INF, INF, 1053],
                [INF, INF, 1364, INF, 0, 1106, INF, INF, INF, 766],
                [343, 879, 1054, INF, 1106, 0, INF, INF, INF, INF],
                [INF, 954, INF, 433, INF, INF, 0, 837, INF, INF],
                [1435, 811, INF, INF, INF, INF, 837, 0, INF, INF],
                [464, INF, INF, INF, INF, INF, INF, INF, 0, INF],
                [INF, 524, INF, 1053, 766, INF, INF, INF, INF, 0]]

        result =  floyd_warshall(graph)
        expected_result = [[0, 1222, 1397, 2609, 1449, 343, 2176, 1435, 464, 1746],
            [1222, 0, 1933, 1387, 1290, 879, 954, 811, 1686, 524],
            [1397, 1933, 0, 3183, 1364, 1054, 2887, 2744, 1861, 2130],
            [2609, 1387, 3183, 0, 1819, 2266, 433, 1270, 3073, 1053],
            [1449, 1290, 1364, 1819, 0, 1106, 2244, 2101, 1913, 766],
            [343, 879, 1054, 2266, 1106, 0, 1833, 1690, 807, 1403],
            [2176, 954, 2887, 433, 2244, 1833, 0, 837, 2640, 1478],
            [1435, 811, 2744, 1270, 2101, 1690, 837, 0, 1899, 1335],
            [464, 1686, 1861, 3073, 1913, 807, 2640, 1899, 0, 2210],
            [1746, 524, 2130, 1053, 766, 1403, 1478, 1335, 2210, 0]]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
