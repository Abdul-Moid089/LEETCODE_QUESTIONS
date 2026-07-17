from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)

        cnt_g = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            total = 0

            for x in range(g, mx + 1, g):
                total += cnt[x]
                cnt_g[g] -= cnt_g[x]

            cnt_g[g] += total * (total - 1) // 2

        prefix = list(accumulate(cnt_g))

        return [bisect_right(prefix, q) for q in queries]