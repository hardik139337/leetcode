from typing import List
import collections


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        r = []
        for i in nums:
            if count[i] > 1:
                continue
            if i - 1 in count or i + 1 in count:
                continue

            r.append(i)

        return r


r = Solution().findLonely([10, 6, 5, 8])
print(r)
