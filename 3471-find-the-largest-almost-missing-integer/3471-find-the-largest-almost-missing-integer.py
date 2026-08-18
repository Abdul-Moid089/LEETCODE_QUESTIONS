from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter(nums)

        if k == n:
            return max(nums)

        if k == 1:
            ans = -1

            for num in nums:
                if count[num] == 1:
                    ans = max(ans, num)

            return ans
        ans = -1

        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans