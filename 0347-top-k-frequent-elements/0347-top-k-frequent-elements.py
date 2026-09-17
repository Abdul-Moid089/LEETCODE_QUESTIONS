class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return [num for num, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
        