from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        numberOfOne = len(grid) + len(grid[0]) - 1

        if numberOfOne % 2 != 0:
            return False
        numberOfOne = numberOfOne / 2

        if grid[0][0] == 0:
            queue = [[0, 0, numberOfOne - 1, numberOfOne]]
        else:
            queue = [[0, 0, numberOfOne, numberOfOne - 1]]

        while queue:
            i = queue.pop(0)
            if i[2] < 0:
                continue
            if i[3] < 0:
                continue
            if i[0] == len(grid) - 1 and i[1] == len(grid[0]) - 1:
                return True
            for j in [[0, 1], [1, 0]]:
                new_var = i[0] + j[0]
                new_var1 = i[1] + j[1]
                if new_var >= len(grid):
                    continue
                if new_var1 >= len(grid[0]):
                    continue
                if grid[new_var][new_var1] == 0:
                    queue.append([new_var, new_var1, i[2] - 1, i[3]])
                else:
                    queue.append([new_var, new_var1, i[2], i[3] - 1])
        return False


r = Solution().isThereAPath([[1, 1, 0], [0, 0, 1], [1, 0, 0]])
print(r)
