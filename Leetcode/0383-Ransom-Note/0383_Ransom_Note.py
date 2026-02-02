class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not magazine and not ransomNote:
            return False

        r = {}
        m = {}
        for i in ransomNote:
            if i not in r:
                r[i] = 1
            else:
                r[i] += 1
        
        for j in magazine:
            if j not in m:
                m[j] = 1
            else:
                m[j] += 1
        
        for c in ransomNote:
            if c in m and m[c] > 0 and r[c] > 0:
                r[c] -= 1
                m[c] -= 1
            else:
                return False

        for i in list(r):
            if r[i] == 0:
                r.pop(i)

        return r == {}