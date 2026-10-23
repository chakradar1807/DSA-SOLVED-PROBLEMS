class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fm=sm=tm=float('-inf')
        for i in nums:
            if i>fm:
                tm=sm
                sm=fm
                fm=i
            elif i>sm and i<fm:
                tm=sm
                sm=i
            elif i>tm and i<sm and i<fm:
                tm=i
        if len(set(nums))<3:
            return max(set(nums))
        return tm