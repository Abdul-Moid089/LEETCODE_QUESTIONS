
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] ^= val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res ^= self.bit[i]
            i -= i & -i
        return res


class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS avoids recursion-depth errors.
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[0][u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        chars = [1 << (ord(c) - ord('a')) for c in s]

        # Difference array using XOR Fenwick Tree.
        bit = FenwickTree(n + 1)

        for u in range(n):
            bit.update(tin[u], chars[u])
            bit.update(tout[u], chars[u])

        ans = []

        for q in queries:
            op, a, b = q.split()
            u = int(a)

            if op == "update":
                new_mask = 1 << (ord(b) - ord('a'))
                delta = chars[u] ^ new_mask

                if delta:
                    bit.update(tin[u], delta)
                    bit.update(tout[u], delta)
                    chars[u] = new_mask

            else:
                v = int(b)
                w = lca(u, v)

                mask = (
                    bit.query(tin[u] + 1)
                    ^ bit.query(tin[v] + 1)
                    ^ chars[w]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
