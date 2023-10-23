from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]
        minDistance = 0
        for i in range(len(stones) - 2):
            minDistance = max(stones[i + 2] - stones[i], minDistance)
        return minDistance
