from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(int)
        for r, s in reservedSeats:
            rows[r] |= 1 << (s - 1)
        ans = (n - len(rows)) * 2
        left = 0b0000011110
        middle = 0b0001111000
        right = 0b0111100000
        for seats in rows.values():
            if seats & left == 0 and seats & right == 0:
                ans += 2
            elif seats & left == 0 or seats & middle == 0 or seats & right == 0:
                ans += 1
        return ans