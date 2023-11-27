from bisect import bisect_right
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])

        startPos = [tiles[i][0] for i in range(len(tiles))]

        preSum = [0] * (len(tiles) + 1)
        for i in range(1, len(tiles) + 1):
            preSum[i] = preSum[i - 1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1)

        res = 0
        for i in range(len(tiles)):
            s, e = tiles[i]

            if e >= s + carpetLen - 1:
                return carpetLen

            endIdx = bisect_right(startPos, s + carpetLen - 1) - 1

            compensate = 0
            if tiles[endIdx][1] > s + carpetLen - 1:
                compensate = tiles[endIdx][1] - s - carpetLen + 1

            res = max(res, preSum[endIdx + 1] - preSum[i] - compensate)

        return res
