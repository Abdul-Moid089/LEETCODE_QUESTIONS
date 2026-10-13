class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        mid = n // 2
        return sum(sq[mid:]) - sum(sq[:mid])