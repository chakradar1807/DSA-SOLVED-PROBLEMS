from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(p)
        s_len = len(s)
        if s_len < n:
            return []
            
        p_count = Counter(p)
        window = Counter()
        left = 0
        
        match_count = 0
        for right in range(s_len):
            window[s[right]] += 1
            if right - left + 1 > n:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == p_count:
                match_count += 1

        ans = [0] * match_count
        
        window.clear()
        left = 0
        idx = 0
        for right in range(s_len):
            window[s[right]] += 1
            if right - left + 1 > n:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == p_count:
                ans[idx] = left
                idx += 1

        return ans       