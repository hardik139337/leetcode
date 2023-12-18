from typing import List


class Solution:
    def minimumCardPickup(self, c: List[int]) -> int:
        r = float("inf")
        m = {}

        for i, v in enumerate(c):
            if v in m:
                r = min(r, i - m[v])
            m[v] = i
        return r + 1 if r != float("inf") else -1


r = Solution().minimumCardPickup([2, 0, 2, 0, 2, 2])
print(r)
