class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = []

        def backtrack(start: int):
            if len(comb) == k:
                res.append(comb.copy())
                return

            need = k - len(comb)
            remain = n - start + 1
            available = remain - need

            for i in range(start, start + available + 1):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return res