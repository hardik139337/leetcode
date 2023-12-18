from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        print(descriptions)
        treeMap = {}
        s = set()
        csset = set()

        for h, c, l in descriptions:
            s.add(h)
            csset.add(c)
            if c in treeMap:
                c = treeMap[c]
            else:
                treeMap[c] = TreeNode(c)
                c = treeMap[c]

            if h in treeMap:
                h = treeMap[h]
            else:
                treeMap[h] = TreeNode(h)
                h = treeMap[h]

            if l:
                h.left = c
            else:
                h.right = c

        r = s - csset
        return treeMap[list(r)[0]]


r = Solution().createBinaryTree(
    [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
)

print(r)
