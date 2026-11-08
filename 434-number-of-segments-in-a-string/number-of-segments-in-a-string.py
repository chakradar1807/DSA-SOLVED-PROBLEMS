class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        inside_segment = False
        
        for char in s:
            if char != ' ' and not inside_segment:
                count += 1
                inside_segment = True
            elif char == ' ' and inside_segment:
                inside_segment = False
        
        return count