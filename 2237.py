from typing import List


class Solution:
    def meetRequirement(
        self, n: int, lights: List[List[int]], requirement: List[int]
    ) -> int:
        d = [0] * n + 1

        for p, r in lights:
            i, j = max(0, p - r), min(n - 1, p + r)
            d[i] += 1
            d[j + 1] -= 1

        for i in range(setattr):
            d[i] += d[i - 1]

        count = 0
        for i in range(requirement):
            if requirement[i] <= d[i]:
                count += 1

        return count
