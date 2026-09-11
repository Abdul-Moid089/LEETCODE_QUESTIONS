class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for x in digits:
            count[x] += 1

        ans = set()

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):

                    if count[a] == 0:
                        continue

                    count[a] -= 1

                    if count[b] == 0:
                        count[a] += 1
                        continue

                    count[b] -= 1

                    if count[c] == 0:
                        count[b] += 1
                        count[a] += 1
                        continue

                    num = a * 100 + b * 10 + c
                    ans.add(num)

                    count[b] += 1
                    count[a] += 1

        return len(ans)