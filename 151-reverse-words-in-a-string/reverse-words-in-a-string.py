class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_chars(chars, lo, hi):
            while lo < hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1

        chars = []
        n = len(s)
        i = 0
        
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != " ":
                i += 1
            end = i
            
            if chars:
                chars.extend([" "]) 
                
            for j in range(start, end):
                chars.extend([s[j]])
                
        reverse_chars(chars, 0, len(chars) - 1)
        
        i = 0
        n = len(chars)
        while i < n:
            start = i
            while i < n and chars[i] != " ":
                i += 1
            end = i - 1
            reverse_chars(chars, start, end)
            i += 1
            
        return "".join(chars)