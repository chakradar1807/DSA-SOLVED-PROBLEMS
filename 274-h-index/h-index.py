class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                counts[n] += 1
            else:
                counts[c] += 1
                
        total_papers = 0
        for i in range(n, -1, -1):
            total_papers += counts[i]
            if total_papers >= i:
                return i
        return 0