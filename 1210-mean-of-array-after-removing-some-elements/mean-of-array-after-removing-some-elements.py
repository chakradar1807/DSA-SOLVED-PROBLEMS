import heapq

class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n = len(arr)
        remove_count = n // 20  
        
        smallest = heapq.nsmallest(remove_count, arr)
        largest = nlargest_vals = heapq.nlargest(remove_count, arr)
        
        total_sum = sum(arr)
        total_sum -= sum(smallest)
        total_sum -= sum(largest)
        
        return total_sum / (n - (2 * remove_count))