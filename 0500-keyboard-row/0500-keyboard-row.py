class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")

        result=[]
        for word in words:

            w_lower =word.lower()
            if w_lower[0] in row1:
                target_row=row1
            elif w_lower[0] in row2:
                target_row = row2
            else:
                target_row=row3

            if all(char in target_row for char in w_lower):
                result.append(word)

        return result