class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        mult_count = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            for m in range(d, max_f + 1, d):
                mult_count[d] += freq[m]

        dp = [0] * (budget + 1)
        for f, price in items:
            if price > budget:
                continue
            free = mult_count[f] - 1
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + 1 + free)
            for b in range(price, budget + 1):
                dp[b] = max(dp[b], dp[b - price] + 1)

        return dp[budget]