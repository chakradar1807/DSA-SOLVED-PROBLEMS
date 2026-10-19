class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(1 for i in range(k) if s[i] in vowels)  

        maxx = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:  
                count -= 1
            if s[i] in vowels:      
                count += 1

            if count > maxx:
                maxx = count

            if count == k:          
                return count

        return maxx