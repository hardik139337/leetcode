from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []

        nums.remove(pivot)

        i = 0
        ans.append(pivot)

        for j in nums:
            if j < pivot:
                ans.insert(i, j)
                i = i + 1
            elif j == pivot:
                ans.insert(i + 1, j)
            else:
                ans.append(j)

        return ans
