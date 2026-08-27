class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for i in range(len(target) - 1, -1, -1):
            used = [0] * 26

            for j in range(i):
                idx = ord(target[j]) - ord('a')
                used[idx] += 1

                if used[idx] > cnt[idx]:
                    break
            else:
                remaining = cnt[:]

                for j in range(i):
                    remaining[ord(target[j]) - ord('a')] -= 1

                curr = ord(target[i]) - ord('a')

                for c in range(curr + 1, 26):
                    if remaining[c] > 0:
                        remaining[c] -= 1

                        ans = list(target[:i])
                        ans.append(chr(c + ord('a')))

                        for x in range(26):
                            ans.extend([chr(x + ord('a'))] * remaining[x])

                        return ''.join(ans)

        return ""