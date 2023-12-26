from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum == 2:
            return [2]
        if finalSum % 2 != 0:
            return []
        r = []
        tsum = finalSum
        for i in range(2, finalSum, 2):
            if i + 2 > tsum - i:
                r.append(tsum)
                return r
            tsum -= i
            r.append(i)

        return r


r = Solution().maximumEvenSplit(28)
print(r)
