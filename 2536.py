from typing import List

import bisect

bisect.bisect([], 1, key=lambda i: i[0])


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        one = [[i[1][0], i[0]] for i in enumerate(queries)]
        two = [[i[1][1], i[0]] for i in enumerate(queries)]
        three = [[i[1][2], i[0]] for i in enumerate(queries)]
        four = [[i[1][3], i[0]] for i in enumerate(queries)]

        one.sort(key=lambda t: t[0])
        two.sort(key=lambda t: t[0])
        three.sort(key=lambda t: t[0])
        four.sort(key=lambda t: t[0])

        for q in range(n):
            for z in range(n):
                index = bisect.bisect_left(one, q, key=lambda l: l[0])
                anwar = set([i[1] for i in one][index:])

                index = bisect.bisect_left(two, q, key=lambda l: l[0])
                anwar = anwar & set([i[1] for i in two][:index])

                index = bisect.bisect_left(three, z, key=lambda l: l[0])
                anwar = anwar & set([i[1] for i in three][index:])

                index = bisect.bisect_left(four, z, key=lambda l: l[0])
                anwar = anwar & set([i[1] for i in four][:index])

                anwar = len(anwar)
                print(anwar)


Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])
