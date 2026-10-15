class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        n = len(nums)
        missing_count = 0
        for i in range(1, n + 1):
            if i not in num_set:
                missing_count += 1
        res = [0] * missing_count
        idx = 0
        
        for i in range(1, n + 1):
            if i not in num_set:
                res[idx] = i
                idx += 1
                
        return res