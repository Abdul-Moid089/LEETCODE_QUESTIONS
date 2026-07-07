from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        solendivar = (s, queries)

        cnt = [0] * (n + 1)
        digit_sum = [0] * (n + 1)
        val = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            cnt[i + 1] = cnt[i]
            digit_sum[i + 1] = digit_sum[i]
            val[i + 1] = val[i]

            if ch != '0':
                d = ord(ch) - ord('0')
                cnt[i + 1] += 1
                digit_sum[i + 1] += d
                val[i + 1] = (val[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            length = cnt[r + 1] - cnt[l]
            sm = digit_sum[r + 1] - digit_sum[l]

            x = (val[r + 1] - val[l] * pow10[length]) % MOD
            ans.append((x * sm) % MOD)

        return ans