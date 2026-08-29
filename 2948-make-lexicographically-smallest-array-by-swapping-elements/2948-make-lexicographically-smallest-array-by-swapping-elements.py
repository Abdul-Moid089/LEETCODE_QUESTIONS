class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * n

        i = 0

        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            indices.sort()

            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans