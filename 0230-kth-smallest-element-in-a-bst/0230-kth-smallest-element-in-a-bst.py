class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.answer = 0

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            self.k -= 1

            if self.k == 0:
                self.answer = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.answer