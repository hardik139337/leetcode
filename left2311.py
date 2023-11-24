class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        kb = "{0:b}".format(k)
        if len(kb) > len(s):
            return len(s)

        if kb >= s[-len(kb) :]:
            count = 0

            for i in s[: -len(kb)]:
                if i == "0":
                    count += 1

            return count + len(kb)

        count = 0

        for i in s[: -len(kb) + 1]:
            if i == "0":
                count += 1

        return count + len(kb) - 1


i = Solution().longestSubsequence("00101001", 1)
print(i)
# 6
