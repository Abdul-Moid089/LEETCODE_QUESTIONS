class Solution:
    def getAllElements(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode]
    ) -> List[int]:

        def inorder(root):
            if not root:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        l1 = inorder(root1)
        l2 = inorder(root2)

        m = len(l1)
        n = len(l2)

        final_l = [0] * (m + n)

        i = 0
        j = 0
        k = 0

        while i < m and j < n:

            if l1[i] <= l2[j]:
                final_l[k] = l1[i]
                i += 1
            else:
                final_l[k] = l2[j]
                j += 1

            k += 1

        while i < m:
            final_l[k] = l1[i]
            i += 1
            k += 1

        while j < n:
            final_l[k] = l2[j]
            j += 1
            k += 1

        return final_l