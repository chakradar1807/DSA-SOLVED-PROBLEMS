class Solution:
    def find_median(self, nums: List[int]) -> int:
        k = len(nums) // 2
        count_array = [0] * 5000
        for val in nums:
            count_array[val] += 1
        for num, count in enumerate(count_array):
            k -= count
            if k < 0:
                return num
    def new_index(self,index, n):
        return (1 + 2 * index) % (n | 1)

    def wiggleSort(self, nums):
        n = len(nums)
        left, i, right = 0, 0, n - 1
        median = self.find_median(nums)
        while i <= right:
            if nums[self.new_index(i, n)] > median:
                k = self.new_index(left, n)
                j = self.new_index(i, n)
                nums[k], nums[j] = nums[j], nums[k] 
                left += 1
                i += 1
            elif nums[self.new_index(i, n)] < median:
                k = self.new_index(right, n)
                j = self.new_index(i, n)
                nums[k], nums[j] = nums[j], nums[k] 
                right -= 1
            else:
                i += 1