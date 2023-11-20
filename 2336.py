from heapq import *


class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 0
        self.added = []
        self.addedSet = set()

    def popSmallest(self) -> int:
        if self.added:
            val = heappop(self.added)
            self.addedSet.remove(val)
            return val
        self.curr += 1
        # rslt=self.nxt
        return self.curr

    def addBack(self, num: int) -> None:
        if num <= self.curr and num not in self.addedSet:
            self.addedSet.add(num)
            heappush(self.added, num)
