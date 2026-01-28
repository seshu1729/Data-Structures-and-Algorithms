class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = []
        goto = 1
        i = j = 0
        
        while i < len(word1) and j < len(word2):
            if goto == 1:
                final.append(word1[i])
                goto = 2
                i += 1
            else:
                final.append(word2[j])
                goto = 1
                j += 1
    
        while i < len(word1):
            final.append(word1[i])
            i += 1
        
        while j < len(word2):
            final.append(word2[j])
            j += 1

        return "".join(final)