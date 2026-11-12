class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        i = 0
        j = i+1
        res = 0
        while i < n and j < n:
            if s[i] == s[j]:
                while j < n:
                    if s[i] == s[j]:
                        j+=1
                    else:
                        break
                res = max(j-i, res)
                i = j
                j = i + 1
            else: 
                i += 1
                j = i + 1
        
        return res if res != 0 else 1