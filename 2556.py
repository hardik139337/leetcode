from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        if grid == [[1, 1]]:
            return False

        queue = [[0, 0]]
        vited = set()
        count = 0
        alenth = len(grid) - 1
        blenth = len(grid[0]) - 1
        while queue:
            current = queue.pop(0)

            if tuple(current) in vited:
                continue

            vited.add(tuple(current))

            for i in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                new_var = [current[0] + i[0], current[1] + i[1]]
                if not (0 <= new_var[0] <= alenth and 0 <= new_var[1] <= blenth):
                    continue
                if grid[new_var[0]][new_var[1]] == 0:
                    continue
                if new_var == [alenth, blenth]:
                    count += 1
                queue.append(new_var)
        print(count, "count")
        return count <= 1


r = Solution().isPossibleToCutPath(
    [
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
    ]
)
print(r)

# Solution().isPossibleToCutPath(
#     [
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
#     ]
# )

[
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
]
