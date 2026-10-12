class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        mod = 10**9 + 7
        for _ in range(k):
            curr = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    curr |= (1 << i)
                    bit_counts[i] -= 1
            ans = (ans + curr * curr) % mod
            
        return ans