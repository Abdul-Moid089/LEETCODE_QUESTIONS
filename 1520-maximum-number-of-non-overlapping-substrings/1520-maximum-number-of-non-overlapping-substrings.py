class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i in range(len(s)):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for l in range(len(s)):
            x = ord(s[l]) - ord('a')

            if first[x] != l:
                continue

            r = last[x]
            i = l
            valid = True

            while i <= r:
                y = ord(s[i]) - ord('a')

                if first[y] < l:
                    valid = False
                    break

                r = max(r, last[y])
                i += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans