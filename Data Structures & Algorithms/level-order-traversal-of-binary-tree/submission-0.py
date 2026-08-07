# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = collections.defaultdict(list)
        def traverse(depth, node):
            if not node: return
            levels[depth].append(node.val)
            traverse(depth + 1, node.left)
            traverse(depth + 1, node.right)

        traverse(0, root)
        out = []
        for v in levels.values():
            out.append(v)
        return out