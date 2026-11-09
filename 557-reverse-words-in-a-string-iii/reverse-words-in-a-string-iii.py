class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_chars(chars, lo, hi):
            while lo < hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1

        chars = list(s)
        n = len(chars)
        start = 0
        
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                reverse_chars(chars, start, i - 1)
                start = i + 1
                
        return "".join(chars)