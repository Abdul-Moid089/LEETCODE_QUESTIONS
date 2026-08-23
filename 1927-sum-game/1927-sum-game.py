class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n):
            if num[i] == '?':
                if i < mid:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < mid:
                    left_sum += int(num[i])
                else:
                    right_sum += int(num[i])

        diff = left_sum - right_sum
        qdiff = right_q - left_q

        return diff != 9 * qdiff / 2