# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        def compare(n1, n2):
            if n1.val != n2.val:
                return False
            
            if n1.left and n2.left:
                if not compare(n1.left, n2.left):
                    return False
            elif n1.left or n2.left:
                return False
            if n1.right and n2.right:
                if not compare(n1.right, n2.right):
                    return False
            elif n1.right or n2.right:
                return False
            
            return True
        
        return compare(p, q)