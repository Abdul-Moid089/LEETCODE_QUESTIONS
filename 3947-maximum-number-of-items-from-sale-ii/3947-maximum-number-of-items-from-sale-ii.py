from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max(factor for factor, _ in items)
        freq = [0] * (max_f + 1)
        min_price = float("inf")

        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price

        # mult_count[x] = count of items whose factor is a multiple of x
        mult_count = [0] * (max_f + 1)
        for x in range(1, max_f + 1):
            if freq[x]:
                total = 0
                for multiple in range(x, max_f + 1, x):
                    total += freq[multiple]
                mult_count[x] = total

        # Each item with `factor` can trigger free copies for `mult_count[factor] - 1` other items
        candidates = []
        for factor, price in items:
            gain = mult_count[factor] - 1
            if gain > 0 and price < 2 * min_price:
                candidates.append((price, gain))

        # Process value-2 marginal units from cheapest price first
        candidates.sort(key=lambda x: x[0])

        total_items = 0
        rem_budget = budget

        for price, gain in candidates:
            if rem_budget < price:
                break
            take = min(gain, rem_budget // price)
            total_items += 2 * take
            rem_budget -= take * price

        # Use remaining budget on the cheapest value-1 units
        total_items += rem_budget // int(min_price)
        return total_items