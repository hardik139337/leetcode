from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []

        for i in nums:
            if dic[i] == 1 and i - 1 not in dic and i + 1 not in dic:
                ans.append(i)

        return ans
