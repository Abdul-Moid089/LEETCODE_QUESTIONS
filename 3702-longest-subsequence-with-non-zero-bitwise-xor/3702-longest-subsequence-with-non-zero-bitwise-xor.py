from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        has_non_zero = False

        for x in nums:
            total_xor ^= x

            if x != 0:
                has_non_zero = True

        if total_xor != 0:
            return n

        if has_non_zero:
            return n - 1

        return 0
        