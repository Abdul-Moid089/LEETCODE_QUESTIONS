from math import gcd

class Solution:
    def findGCD(self, nums: List[int]):
        return gcd(min(nums), max(nums))