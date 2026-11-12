class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
    	b = 1
    	while b:
    		b, i, c = 0, 0, 1
    		while i < len(s)-1:
    			i += 1
    			if s[i] == s[i-1]: c += 1
    			else: c = 1
    			if c == k: s, b, i, c = s[:i-k+1]+s[i+1:], 1, max(0,i-k), 1 
    	return s

	