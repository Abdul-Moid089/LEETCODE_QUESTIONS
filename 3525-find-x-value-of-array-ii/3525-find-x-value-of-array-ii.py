class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [None] * (4 * n)

        def merge(a, b):
            ap, ac = a
            bp, bc = b

            prod = (ap * bp) % k
            cnt = ac[:]

            for r in range(k):
                cnt[(ap * r) % k] += bc[r]

            return [prod, cnt]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                cnt = [0] * k
                cnt[v] = 1
                tree[node] = [v, cnt]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, pos, value):
            if l == r:
                v = value % k
                cnt = [0] * k
                cnt[v] = 1
                tree[node] = [v, cnt]
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start, n - 1)

            ans.append(result[1][x])

        return ans