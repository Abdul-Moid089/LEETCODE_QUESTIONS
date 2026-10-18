class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def countWays(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways_left = countWays(left)
            ways_right = countWays(right)
            
            comb = math.comb(len(left) + len(right), len(left))
            
            return (comb * ways_left * ways_right) % MOD

        import math
        return (countWays(nums) - 1 + MOD) % MOD