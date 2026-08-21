from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = list(set(coins))

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        if multiple > x:
                            valid = False
                            break
                        bits += 1

                if valid:
                    if bits % 2:
                        total += x // multiple
                    else:
                        total -= x // multiple

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

        