class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        d = {}

        def rec(root):
            if root is None:
                return

            rec(root.left)

            d[root.val] = d.get(root.val, 0) + 1

            rec(root.right)

        rec(root)

        result = []

        max_freq = 0

        for key in d:
            max_freq = max(max_freq, d[key])

        for key in d:
            if d[key] == max_freq:
                result.append(key)

        return result