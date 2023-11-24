from typing import List
import collections


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = collections.defaultdict(int)

        for i in range(len(messages)):
            c = messages[i].count(" ") + 1
            count[senders[i]] += c
        maxR = 0
        r = []
        for i in count:
            if count[i] > maxR:
                r = [i]
                maxR = count[i]

            if count[i] == maxR:
                r.append(i)
        r.sort()
        return r[-1]


r = Solution().largestWordCount(
    ["How is leetcode for everyone", "Leetcode is useful for practice"],
    ["Bob", "Charlie"],
)
print(r)
