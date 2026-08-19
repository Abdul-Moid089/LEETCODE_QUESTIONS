class Solution:
    def convertBST(self, root):
        total = 0

        def dfs(node):
            nonlocal total

            if not node:
                return

            dfs(node.right)

            total += node.val
            node.val = total

            dfs(node.left)

        dfs(root)

        return root