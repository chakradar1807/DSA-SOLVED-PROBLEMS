class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        n = len(heights)
        
        newheights = heights[:]
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if newheights[j] > newheights[j + 1]:
                    newheights[j], newheights[j + 1] = newheights[j + 1], newheights[j]
                    swapped = True
            if not swapped:
                break

        count = 0
        for i in range(n):
            if heights[i] != newheights[i]:
                count += 1
                
        return count