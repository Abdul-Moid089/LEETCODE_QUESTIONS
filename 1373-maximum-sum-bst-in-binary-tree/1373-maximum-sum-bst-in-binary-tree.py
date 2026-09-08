class Solution:
    def maxSumBST(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            # Empty tree is a valid BST
            if node is None:
                return True, float('inf'), float('-inf'), 0

            # Get information from left and right
            leftBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightBST, rightMin, rightMax, rightSum = dfs(node.right)

            # Check if current subtree is a BST
            if leftBST and rightBST and leftMax < node.val < rightMin:

                currentSum = leftSum + node.val + rightSum

                ans = max(ans, currentSum)

                currentMin = min(leftMin, node.val)
                currentMax = max(rightMax, node.val)

                return True, currentMin, currentMax, currentSum

            # Not a BST
            return False, 0, 0, 0

        dfs(root)

        return ans