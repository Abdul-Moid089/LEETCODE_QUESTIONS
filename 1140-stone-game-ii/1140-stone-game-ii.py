from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # exact[i] = latest possible position of word2[i]
        # when word2[i:] is matched exactly.
        exact = [n] * (m + 1)

        j = n - 1

        for i in range(m - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1

            if j < 0:
                break

            exact[i] = j
            j -= 1

        # almost[i] = latest possible position of word2[i]
        # when word2[i:] can have at most one mismatch.
        almost = [n] * (m + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Match this character exactly.
                # The remaining part may contain one mismatch.
                if word1[j] == word2[i]:
                    if j < almost[i + 1]:
                        almost[i] = j
                        break

                # Use the one mismatch here.
                # The remaining part must match exactly.
                else:
                    if j < exact[i + 1]:
                        almost[i] = j
                        break

        # Greedily construct lexicographically smallest indices.
        ans = []
        pos = 0
        mismatch_used = False

        for i in range(m):

            while pos < n:

                # Match exactly.
                if word1[pos] == word2[i]:

                    # Remaining characters can still be matched
                    # with at most one mismatch.
                    if pos < almost[i + 1]:
                        ans.append(pos)
                        pos += 1
                        break

                # Use our one allowed mismatch.
                elif not mismatch_used:

                    # Remaining characters must match exactly.
                    if pos < exact[i + 1]:
                        ans.append(pos)
                        pos += 1
                        mismatch_used = True
                        break

                pos += 1

            else:
                return []

        return ans