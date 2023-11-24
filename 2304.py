from typing import List
import functools


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        lenrow = len(grid[0])

        @functools.cache
        def dfs(i, j):
            if i == len(grid) - 1:
                return grid[i][j]
            new_var = grid[i][j]
            m = min([dfs(i + 1, q) + moveCost[new_var][q] for q in range(lenrow)])

            return grid[i][j] + m

        return min([dfs(0, i) for i in range(lenrow)])


t = Solution().minPathCost(
    [[5, 3], [4, 0], [2, 1]], [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
)

print(t)
