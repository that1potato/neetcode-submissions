# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(node, subnode):
            if node is None and subnode is None:
                return True
            elif node is None or subnode is None:
                return False

            if node.val != subnode.val:
                return False

            lres = traverse(node.left, subnode.left)
            rres = traverse(node.right, subnode.right)
            return lres and rres

        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if traverse(cur, subRoot):
                    return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
            