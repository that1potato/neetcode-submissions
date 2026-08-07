# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_search = []
        q_search = []
        def traverse(n, cur, search_tree):
            search_tree.append(cur)
            if cur is None or n.val == cur.val:
                return 
            elif n.val < cur.val:
                traverse(n, cur.left, search_tree)
            else:
                traverse(n, cur.right, search_tree)
        
        traverse(p, root, p_search)
        traverse(q, root, q_search)

        # compare search tree
        lca = root
        i = 0
        while i < len(p_search) and i < len(q_search):
            if p_search[i].val == q_search[i].val:
                lca = p_search[i]
            i += 1

        return lca