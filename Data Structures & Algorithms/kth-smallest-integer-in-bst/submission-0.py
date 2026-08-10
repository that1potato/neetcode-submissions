# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mid_retrieval = []
        def retrieve(node):
            if node.left:
                retrieve(node.left)
            mid_retrieval.append(node.val)
            if node.right:
                retrieve(node.right)
        retrieve(root)
        return mid_retrieval[k-1]