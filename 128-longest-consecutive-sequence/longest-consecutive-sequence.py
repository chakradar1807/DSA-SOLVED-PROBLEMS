class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_length = 1
        x = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                x += 1
                if x > max_length:
                    max_length = x
            elif nums[i + 1] == nums[i]:
                continue
            else:
                x = 1

        return max_length
        