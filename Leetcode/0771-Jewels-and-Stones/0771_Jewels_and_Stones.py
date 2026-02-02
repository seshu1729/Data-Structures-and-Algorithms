class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = {}
        s = {}
        for i in jewels:
            if i not in j:
                j[i] = 0
                j[i] += 1
            else:
                j[i] += 1
            
        for i in stones:
            if i not in s:
                s[i] = 0
                s[i] += 1
            else:
                s[i] += 1
        sum = 0
        for i in s:
            if i in j:
                sum += s[i]

        return sum