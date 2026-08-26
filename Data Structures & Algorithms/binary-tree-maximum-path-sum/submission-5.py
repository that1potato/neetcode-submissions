# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -float('inf')

        def bottom_sum(node):
            nonlocal best
            
            if node is None:
                return 0
            
            left_sum = bottom_sum(node.left)
            right_sum = bottom_sum(node.right)
            
            cur_sum = max(
                left_sum + node.val,
                right_sum + node.val,
                node.val
            )
            best = max(best, cur_sum, left_sum + node.val + right_sum)
            return cur_sum
        
        bottom_sum(root)
        return best
            