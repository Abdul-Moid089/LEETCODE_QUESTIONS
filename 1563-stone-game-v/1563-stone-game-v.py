from functools import cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(i, j):
            if i >= j:
                return 0

            ans = 0
            left_sum = 0
            total = prefix[j + 1] - prefix[i]
            right_sum = total

            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    # Bob removes right part.
                    # Alice gets left_sum.
                    if ans >= left_sum * 2:
                        continue

                    ans = max(
                        ans,
                        left_sum + dp(i, k)
                    )

                elif left_sum > right_sum:
                    # Bob removes left part.
                    # Alice gets right_sum.
                    if ans >= right_sum * 2:
                        break

                    ans = max(
                        ans,
                        right_sum + dp(k + 1, j)
                    )

                else:
                    # Both parts have equal sum.
                    ans = max(
                        ans,
                        left_sum + dp(i, k),
                        right_sum + dp(k + 1, j)
                    )

            return ans

        return dp(0, len(stoneValue) - 1)