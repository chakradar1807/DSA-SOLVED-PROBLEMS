class Solution:
    def concatWithReverse(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        
        for i in range(n):
            result[i] = nums[i]
            
        for i in range(n):
            result[n + i] = nums[n - 1 - i]
            
        return result