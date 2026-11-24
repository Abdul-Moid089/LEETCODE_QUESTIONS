import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        
        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            
            for j in range(i + 1, n):
                curr_prod *= nums[j]
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])
                
                if curr_prod == curr_gcd * curr_lcm:
                    ans = max(ans, j - i + 1)
                elif curr_prod > 2520 * curr_gcd:
                    break
                    
        return ans