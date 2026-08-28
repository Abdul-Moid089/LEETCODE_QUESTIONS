class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # A palindrome is possible only with at most one odd frequency.
        odd = [i for i in range(26) if freq[i] % 2]

        if len(odd) > 1:
            return ""

        half_count = [x // 2 for x in freq]
        m = n // 2

        middle = ""
        if n % 2:
            middle = chr(odd[0] + ord('a'))

        def build(left):
            return left + middle + left[::-1]

        def smallest_half():
            res = []
            for i in range(26):
                res.append(chr(i + ord('a')) * half_count[i])
            return ''.join(res)

        def make_greater_half(t):
            """
            Return the smallest permutation of half_count
            that is strictly greater than t.
            """
            m = len(t)

            for pos in range(m - 1, -1, -1):
                remaining = half_count[:]

                # Try to match t[0:pos].
                possible = True

                for i in range(pos):
                    c = ord(t[i]) - ord('a')

                    if remaining[c] == 0:
                        possible = False
                        break

                    remaining[c] -= 1

                if not possible:
                    continue

                current = ord(t[pos]) - ord('a')

                # Put the smallest available character
                # that is greater than t[pos].
                for c in range(current + 1, 26):
                    if remaining[c] == 0:
                        continue

                    remaining[c] -= 1

                    suffix = []
                    for x in range(26):
                        suffix.append(
                            chr(x + ord('a')) * remaining[x]
                        )

                    return (
                        t[:pos]
                        + chr(c + ord('a'))
                        + ''.join(suffix)
                    )

            return ""

        # Smallest possible palindrome.
        smallest = smallest_half()
        palindrome = build(smallest)

        if palindrome > target:
            return palindrome

        target_left = target[:m]

        # Check whether target_left itself is a valid half.
        remaining = half_count[:]
        valid = True

        for ch in target_left:
            c = ord(ch) - ord('a')

            if remaining[c] == 0:
                valid = False
                break

            remaining[c] -= 1

        if valid:
            # target_left is a valid permutation.
            # Its palindrome may already be greater than target.
            palindrome = build(target_left)

            if palindrome > target:
                return palindrome

        # Otherwise find the smallest half strictly greater
        # than target_left.
        left = make_greater_half(target_left)

        if not left:
            return ""

        return build(left)