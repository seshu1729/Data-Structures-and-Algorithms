class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        s = []
        len1 = len(word1)
        len2 = len(word2)

        while i < len1 or i < len2:
            if i < len1:
                s.append(word1[i])
            if i < len2:
                s.append(word2[i])
            i += 1

        return "".join(s)