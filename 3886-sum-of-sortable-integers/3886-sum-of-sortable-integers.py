class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True
            prev_max = float("-inf")

            for start in range(0, n, k):
                end = start + k

                descents = 0

                # Check if this block is a cyclic rotation
                # of a sorted array.
                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        descents += 1

                        if descents > 1:
                            possible = False
                            break

                if not possible:
                    break

                # If there is one descent, the last element
                # must be <= the first element.
                if descents == 1 and nums[end - 1] > nums[start]:
                    possible = False
                    break

                # Check that this block comes after the
                # previous block in sorted order.
                block_min = min(nums[start:end])
                block_max = max(nums[start:end])

                if prev_max > block_min:
                    possible = False
                    break

                prev_max = block_max

            if possible:
                ans += k

        return ans