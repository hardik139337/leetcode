from typing import List
import functools


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = {}

        for i in range(len(messages)):
            c = messages[i].count(" ") + 1
            if senders[i] in count:
                count[senders[i]] += c
            else:
                count[senders[i]] = c

        return messages
