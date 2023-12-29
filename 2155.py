from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroCount = 0

        for i in nums:
            if i == 0:
                zeroCount += 1

        oneCount = len(nums) - zeroCount
        tzeroCount = 0
        toneCount = 0
        maxR = 0
        maxRArr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                tzeroCount += 1
            else:
                toneCount += 1
            tsum = toneCount + oneCount - toneCount

            if tsum == maxR:
                maxRArr.append(i)
            if tsum > maxR:
                maxRArr = [i]

        return maxRArr


r = Solution().maxScoreIndices([0, 0, 1, 0])
print(r)
