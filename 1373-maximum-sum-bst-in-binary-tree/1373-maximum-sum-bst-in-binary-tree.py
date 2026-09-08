class Solution:
    def maxSumBST(self, root):
        ans = 0

        def dfs(node):
            nonlocal ans

            if node is None:
                return True, float('inf'), float('-inf'), 0

            leftBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightBST, rightMin, rightMax, rightSum = dfs(node.right)

            if leftBST and rightBST and leftMax < node.val < rightMin:

                currentSum = leftSum + node.val + rightSum

                ans = max(ans, currentSum)

                currentMin = min(leftMin, node.val)
                currentMax = max(rightMax, node.val)

                return True, currentMin, currentMax, currentSum

            return False, 0, 0, 0

        dfs(root)

        return ans