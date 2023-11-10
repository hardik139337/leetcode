from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in nums:
            if i == 0:
                count += 1
            else:
                total += count * (count + 1) / 2
                count = 0
        total += count * (count + 1) / 2
        return total


r = Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0])
print(r)
