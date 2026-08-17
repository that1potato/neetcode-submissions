class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(ino_lo, ino_hi):
            if ino_lo > ino_hi:
                return None
            root = preorder[self.pre_idx]
            self.pre_idx += 1
            k = indices[root]
            node = TreeNode(root)
            node.left  = build(ino_lo, k - 1)
            node.right = build(k + 1, ino_hi)
            return node

        return build(0, len(inorder) - 1)