class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def canPlace(dist):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= dist:
                    count += 1
                    last = position[i]

                    if count == m:
                        return True

            return False

        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if canPlace(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans