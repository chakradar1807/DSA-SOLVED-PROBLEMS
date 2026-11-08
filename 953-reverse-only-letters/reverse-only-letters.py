class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l,r = 0, len(s) - 1
        while (l < r): 
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                s[r], s[l] = s[l], s[r]
                l += 1
                r -= 1
        return ''.join(s)