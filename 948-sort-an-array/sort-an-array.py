class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            n = len(nums)
            if n <= 1:
                return nums
            mid = n // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+= 1
            while j < len(right):
                nums[k] = right[j]
                j+=1
                k += 1
            return nums
        return merge(nums)
            