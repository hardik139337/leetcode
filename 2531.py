from typing import List
import functools


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        alen = len(grid)
        blen = len(grid[0])
        oneCount = alen + blen - 1
        if oneCount % 2 != 0:
            return False
        oneCount = oneCount / 2

        # @functools.cache
        def dfs(i, j, k):
            if i >= alen or j >= blen:
                return False
            if k > oneCount:
                return False
            if i == alen - 1 and j == blen - 1 and k == oneCount:
                return True
            new_var = k + grid[i][j]
            return dfs(i + 1, j, new_var) or dfs(i, j + 1, new_var)

        return dfs(0, 0, 0)


r = Solution().isThereAPath([[0, 1, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0]])
print(r)
