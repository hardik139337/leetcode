from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]

        for i in queries:
            row1, col1, row2, col2 = i
            for j in range(row1, row2 + 1):
                arr[j][col1] += 1
                if col2 + 1 < n:
                    arr[j][col2 + 1] += -1

        for i in range(n):
            for j in range(1, n):
                arr[i][j] += arr[i][j - 1]

        return arr


Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])

[
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
    [2, 2, 5, 5, 4, 4, 4, 2, 2, 2, 1, 0, 0],
    [2, 2, 5, 7, 6, 6, 6, 4, 3, 3, 2, 1, 1],
    [2, 2, 4, 6, 8, 8, 8, 4, 3, 3, 2, 1, 1],
    [2, 2, 4, 6, 8, 8, 8, 4, 3, 3, 2, 1, 1],
    [2, 2, 4, 6, 8, 8, 8, 4, 3, 3, 2, 1, 1],
    [2, 2, 2, 4, 4, 4, 4, 5, 3, 3, 2, 1, 1],
    [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1],
    [2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 4, 2, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 6, 3, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 4, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
]

[
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    [0, 1, 3, 3, 2, 2, 2, 2, 3, 3, 2, 2, 2],
    [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
    [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
    [0, 1, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 4],
    [0, 1, 3, 3, 2, 3, 3, 2, 2, 1, 0, 0, 1],
    [0, 0, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 1],
    [0, 0, 2, 3, 3, 3, 3, 2, 2, 2, 1, 2, 1],
    [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 3, 4, 3],
    [0, 0, 1, 2, 2, 3, 4, 4, 3, 3, 2, 2, 1],
    [0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0],
]


a, b = [1, 2]
a
b
