
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # leaf node chck krna is must
        if not root.left and not root.right:
            return targetSum == root.val

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )
