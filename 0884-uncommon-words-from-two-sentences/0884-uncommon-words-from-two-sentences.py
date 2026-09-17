class Solution:
    def uncommonFromSentences(self, s1, s2):
        words = (s1 + " " + s2).split()
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        return [word for word in words if freq[word] == 1]