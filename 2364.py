from typing import List


import collections


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = collections.defaultdict(0)

        for i in range(len(nums)):
            count[nums[i] - i] += 1
        total = self.new_method(len(nums))
        for i in count:
            total -= self.new_method(count[i])

        return total

    def new_method(self, nums):
        return nums * (nums - 1) / 2
