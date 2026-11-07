class Solution:
    def capitalizeTitle(self, title: str) -> str:
        chars = [ch for ch in title]
        n = len(chars)
        
        i = 0
        while i < n:
            start = i
            while i < n and chars[i] != " ":
                i += 1
            end = i
            
            length = end - start
            
            if length <= 2:
                for j in range(start, end):
                    if 65 <= ord(chars[j]) <= 90:
                        chars[j] = chr(ord(chars[j]) + 32)
            else:
                if 97 <= ord(chars[start]) <= 122: 
                    chars[start] = chr(ord(chars[start]) - 32)
                
                for j in range(start + 1, end):
                    if 65 <= ord(chars[j]) <= 90:
                        chars[j] = chr(ord(chars[j]) + 32)
                        
            i += 1
            
        return "".join(chars)