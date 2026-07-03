from typing import List
from heapq import heappush, heappop
from math import inf

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]

        lo = inf
        hi = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            graph[u].append((v, w))
            lo = min(lo, w)
            hi = max(hi, w)

        if lo == inf:
            return -1

        def check(mid):
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]

            while pq:
                d, u = heappop(pq)

                if d > dist[u]:
                    continue

                if d > k:
                    continue

                if u == n - 1:
                    return True

                for v, w in graph[u]:
                    if w < mid:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans