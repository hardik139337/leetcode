class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.right = None
        self.val = val


def build_binary_tree_from_list(lst, index):
    if index < len(lst):
        if lst[index] is None:
            return None
        node = TreeNode(lst[index])
        node.left = build_binary_tree_from_list(lst, 2 * index + 1)
        node.right = build_binary_tree_from_list(lst, 2 * index + 2)
        return node
    return None


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


input_list = [6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14]
root = build_binary_tree_from_list(input_list, 0)


print_tree(root)


from typing import List, Optional


class Solution:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        # print(root)
        return []


Solution().closestNodes(root, [2, 5, 16])
