import bisect
from collections import defaultdict
from typing import List


class Solution:
    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        def is_contain(rect: List[int], point: List[int]) -> bool:
            return (
                point[0] >= 0
                and point[1] >= 0
                and point[0] <= rect[0]
                and point[1] <= rect[1]
            )

        res = []
        for point in points:
            count = 0
            for rect in rectangles:
                if is_contain(rect, point):
                    count += 1
            res.append(count)

        return res

    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        MAX_HEIGH = 100

        grid = [[] for _ in range(MAX_HEIGH + 1)]
        for rect in rectangles:
            grid[rect[1]].append(rect[0])

        grid[MAX_HEIGH].sort()
        for i in range(MAX_HEIGH - 1, -1, -1):
            grid[i].extend(grid[i + 1])
            grid[i].sort()

        res = []
        for point in points:
            i = bisect.bisect_left(grid[point[1]], point[0])
            res.append(len(grid[point[1]]) - i)
        return res
