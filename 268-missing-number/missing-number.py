class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sum1 = n * (n + 1) // 2
        sum2 = 0

        for i in range(n):
            sum2 += nums[i]

        return sum1 - sum2