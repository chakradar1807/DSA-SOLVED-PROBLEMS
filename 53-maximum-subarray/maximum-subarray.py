class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        
        for i in nums[1:]:
            if i > cur_sum + i:
                cur_sum = i
            else:
                cur_sum = cur_sum + i
                
            if cur_sum > max_sum:
                max_sum = cur_sum
                
        return max_sum