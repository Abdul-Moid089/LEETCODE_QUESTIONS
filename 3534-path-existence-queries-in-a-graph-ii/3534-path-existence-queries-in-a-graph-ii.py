from typing import List

class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:

        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        arr = [0] * n

        for i, idx in enumerate(order):
            pos[idx] = i
            arr[i] = nums[idx]

        nxt = list(range(n))
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1] - arr[i] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = n.bit_length()
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if l == r:
                ans.append(0)
                continue

            if nxt[l] == l:
                ans.append(-1)
                continue

            cur = l
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    dist += 1 << k

            if nxt[cur] >= r:
                ans.append(dist + 1)
            else:
                ans.append(-1)

        return ans