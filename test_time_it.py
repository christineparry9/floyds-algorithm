from main import *

import timeit

def test_function():
    graph = [
            [0, 3, 7, 5],
            [2, 0, 6, 4],
            [3, 1, 0, 5],
            [5, 3, 2, 0]
        ]
    floyd_warshall(graph)

if __name__ == "__main__":
    print("Starting timeit test...")
    time_result = timeit.timeit("test_function()", setup="from __main__ import test_function", number=10000)
    print(f"The function took an average of {time_result / 1000} seconds to run.")
