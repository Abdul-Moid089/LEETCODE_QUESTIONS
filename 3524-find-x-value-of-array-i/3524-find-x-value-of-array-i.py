class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:

            rem = num % k

            new_dp = [0] * k

            new_dp[rem] += 1

            for old_rem in range(k):

                new_rem = (old_rem * rem) % k

                new_dp[new_rem] += dp[old_rem]

            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans