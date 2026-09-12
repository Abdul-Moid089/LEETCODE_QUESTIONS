class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = []
        for i in range(n):
            arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, weight, idx = arr[i - 1]

            p = bisect_left(ends, start, 0, i - 1)

            for j in range(5):
                dp[i][j] = dp[i - 1][j]

                if j > 0:
                    old_score, old_ids = dp[p][j - 1]
                    new_score = old_score + weight
                    new_ids = sorted(old_ids + [idx])

                    if new_score > dp[i][j][0] or (
                        new_score == dp[i][j][0]
                        and new_ids < dp[i][j][1]
                    ):
                        dp[i][j] = (new_score, new_ids)

        answer = (0, [])

        for j in range(5):
            if dp[n][j][0] > answer[0] or (
                dp[n][j][0] == answer[0]
                and dp[n][j][1] < answer[1]
            ):
                answer = dp[n][j]

        return answer[1]