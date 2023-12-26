from typing import List
import functools, collections


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for i in edges:
            graph[i[1]].append(i[0])

        @functools.cache
        def dfs(i):
            r = set()
            for j in graph[i]:
                r.add(j)
                for t in dfs(j):
                    r.add(t)

            return r

        return [sorted(list(dfs(i))) for i in range(n)]


a = Solution().getAncestors(
    8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
)

print(a)
