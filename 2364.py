from typing import List


import collections


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = collections.Counter(value - index for index, value in enumerate(nums))

        lenNums = len(nums)

        total = lenNums * (lenNums - 1) / 2
        for i in count.values():
            total -= i * (i - 1) / 2
        print(collections.Counter)
        return total
