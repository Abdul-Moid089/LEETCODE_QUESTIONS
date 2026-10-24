class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        misplaced_and = -1
        
        for i, val in enumerate(nums):
            if val != i:
                if misplaced_and == -1:
                    misplaced_and = val
                else:
                    misplaced_and &= val
                    
        return misplaced_and if misplaced_and != -1 else 0