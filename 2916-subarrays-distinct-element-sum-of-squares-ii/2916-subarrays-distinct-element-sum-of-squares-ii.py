class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if tree_lazy[node] != 0:
                val = tree_lazy[node]
                mid = (l + r) // 2
                
                left_child = 2 * node
                right_child = 2 * node + 1
                
                tree_sum[left_child] = (tree_sum[left_child] + val * (mid - l + 1)) % MOD
                tree_lazy[left_child] = (tree_lazy[left_child] + val) % MOD
                
                tree_sum[right_child] = (tree_sum[right_child] + val * (r - mid)) % MOD
                tree_lazy[right_child] = (tree_lazy[right_child] + val) % MOD
                
                tree_lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                tree_sum[node] = (tree_sum[node] + val * (r - l + 1)) % MOD
                tree_lazy[node] = (tree_lazy[node] + val) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD

        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree_sum[node]
            
            push(node, l, r)
            mid = (l + r) // 2
            res = (query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)) % MOD
            return res

        last = {}
        ans = 0
        current_sum_squares = 0
        
        for j in range(n):
            x = nums[j]
            i = last.get(x, -1) + 1
            last[x] = j
            
            linear_sum = query(1, 0, n - 1, i, j)
            current_sum_squares = (current_sum_squares + 2 * linear_sum + (j - i + 1)) % MOD
            
            update(1, 0, n - 1, i, j, 1)
            ans = (ans + current_sum_squares) % MOD
            
        return ans