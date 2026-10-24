class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Check if a valid partition is possible:
        # 1. target + total_sum must be non-negative
        # 2. target + total_sum must be even
        # 3. abs(target) must not exceed total_sum
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0
            
        subset_sum = (target + total_sum) // 2
        
        # dp[i] stores the number of ways to achieve sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to get a sum of 0 (using empty subset)
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]