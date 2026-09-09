class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        commas = 1

        while True:
            start = 10 ** (3 * commas)

            if start > n:
                break

            ans += n - start + 1
            commas += 1

        return ans