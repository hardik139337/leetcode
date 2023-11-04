class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        Set = set(nums)
        for n in nums:
            strN = str(n)
            strR = strN[::-1]
            Set.add(int(strR))

        return len(Set)
