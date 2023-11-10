from heapq import heappush, heappop


class NumberContainers:
    def __init__(self):
        self.a = {}
        self.b = {}

    def change(self, x: int, y: int) -> None:
        self.a[x] = y
        if y in self.b:
            heappush(self.b[y], x)
        else:
            self.b[y] = [x]

    def find(self, x: int) -> int:
        if x not in self.b:
            return -1
        d = self.b[x]
        while d and self.a[d[0]] != x:
            heappop(d)
        return d[0] if d else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
