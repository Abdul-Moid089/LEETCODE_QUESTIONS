class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        best = [float('inf')] * n
        ans = float('inf')

        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if right > 0:
                best[right] = best[right - 1]

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                best[right] = min(best[right], length)

        return -1 if ans == float('inf') else ans