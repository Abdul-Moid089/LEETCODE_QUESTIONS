class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        
        n = len(s)
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        if s.count(max_char) == 1 and s[0] == max_char and s.count(min_char) == 1 and s[-1] == min_char:
            return 3
            
        return 2