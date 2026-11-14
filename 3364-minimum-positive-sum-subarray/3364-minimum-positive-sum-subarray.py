class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = sum(nums[i:i + length])
                if s > 0:
                    ans = min(ans, s)
        return ans if ans != float('inf') else -1