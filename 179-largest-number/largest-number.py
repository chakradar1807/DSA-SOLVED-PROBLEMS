class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        n = len(nums)

        if sum(nums) == 0:
            return "0"

        nums = list(map(str, nums))

        if len(nums) <= 1:
            return "".join(nums)
        def compar(start, y):
            return (nums[start] + nums[y]) < (nums[y] + nums[start])
           
        for start in range(n):

            y = start + 1
            while y < n:
                
                if compar(start, y):
                    nums[start], nums[y] = nums[y], nums[start]
                y += 1

        return "".join(nums)