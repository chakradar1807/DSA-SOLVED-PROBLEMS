class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        
        for s in strs:
            chars = list(s)
            chars.sort()
            key = "".join(chars)
            
            if key not in d:
                d[key] = [s]
            else:
                d[key] = d[key] + [s]
                
        return [d[key] for key in d]  