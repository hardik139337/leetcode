class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a = 0
        b = 0

        while a < len(start) and b < len(target):
            while start[a] == "_":
                a += 1

            while target[b] == "_":
                b += 1

            if start[a] != target[b]:
                return False
            else:
                a += 1
                b += 1
        if a != len(start):
            for i in start[a:]:
                if i != "_":
                    return False

        if b != len(target):
            for i in target[b:]:
                if i != "_":
                    return False

        return True


a = Solution().canChange("_L__R__R_", "L______RR")
print(a)
