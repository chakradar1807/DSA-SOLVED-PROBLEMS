class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = {}
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
            
        for i in range(len(s)):
            if count_map[s[i]] == 1:
                return i
                
        return -1