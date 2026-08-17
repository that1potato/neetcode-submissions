class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def divide_and_build(ino_lo, ino_hi):
            # ino_lo, ino_hi = boundaries of this subtree within the original inorder
            if ino_lo > ino_hi:
                return None

            # preorder hands out roots in exactly this order
            root = preorder[self.pre_idx]
            self.pre_idx += 1
            # absolute index — no offset needed, nothing was sliced
            root_idx_ino = indices[root]
            node = TreeNode(
                val = root,
                left = divide_and_build(ino_lo, root_idx_ino - 1),
                right = divide_and_build(root_idx_ino + 1, ino_hi)
            )
            return node

        indices = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        return divide_and_build(0, len(inorder) - 1)