class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        # nums.sort()
        if target in nums:
            return True 
        else:
            return False
            