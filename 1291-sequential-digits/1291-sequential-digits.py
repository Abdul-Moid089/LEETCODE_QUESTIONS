from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        for start in range(1, 10):
            num = start

            for nxt in range(start + 1, 10):
                num = num * 10 + nxt

                if low <= num <= high:
                    ans.append(num)

        ans.sort()
        return ans