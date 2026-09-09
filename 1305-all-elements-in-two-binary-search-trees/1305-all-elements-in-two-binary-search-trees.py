class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:

        def inorder(root):
            if not root:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        l1 = inorder(root1)
        l2 = inorder(root2)

        final_l = l1 + l2
        final_l.sort()

        return final_l