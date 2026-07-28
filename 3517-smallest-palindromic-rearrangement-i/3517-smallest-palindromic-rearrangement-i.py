class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        left = sorted(s[: n // 2])

        if n % 2:
            return "".join(left) + s[n // 2] + "".join(left[::-1])

        return "".join(left) + "".join(left[::-1])