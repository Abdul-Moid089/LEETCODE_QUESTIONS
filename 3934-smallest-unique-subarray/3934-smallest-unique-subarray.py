class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base1, base2 = 1_000_003, 1_000_033

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i, val in enumerate(nums):
            h1[i + 1] = (h1[i] * base1 + val) % mod1
            h2[i + 1] = (h2[i] * base2 + val) % mod2
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2

        def has_unique(length: int) -> bool:
            freq: dict[tuple[int, int], int] = {}
            pow1 = p1[length]
            pow2 = p2[length]

            for i in range(n - length + 1):
                a = (h1[i + length] - h1[i] * pow1) % mod1
                b = (h2[i + length] - h2[i] * pow2) % mod2
                key = (a, b)
                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans