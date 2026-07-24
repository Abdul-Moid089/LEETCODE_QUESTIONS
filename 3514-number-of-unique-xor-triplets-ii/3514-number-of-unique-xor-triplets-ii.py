from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = list(set(nums))  # remove duplicates
        m = max(nums).bit_length()
        size = 1 << m

        pair = [False] * size
        for x in nums:
            for y in nums:
                pair[x ^ y] = True

        triplet = [False] * size
        for xy in range(size):
            if pair[xy]:
                for z in nums:
                    triplet[xy ^ z] = True

        return sum(triplet)