from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def dfs(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True
            grid[i][j] = 0
            for t in [[1, 0], [0, 1]]:
                new_var = i + t[0]
                new_var1 = j + t[1]
                if not (0 <= new_var < len(grid) and 0 <= new_var1 < len(grid[0])):
                    continue
                if grid[new_var][new_var1] and dfs(new_var, new_var1):
                    return True
            return False

        if not dfs(0, 0):
            return True
        grid[0][0] = 1
        return not dfs(0, 0)


r = Solution().isPossibleToCutPath(
    [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 1],
    ]
)
print(r)
