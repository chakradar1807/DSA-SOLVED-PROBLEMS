class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_count = {}
        for num in arr:
            arr_count[num] = arr_count.get(num, 0) + 1
            
        lucky = 0
        for i, count in arr_count.items():
            if count > lucky and count == i:
                lucky = count
                
        if lucky != 0:
            return lucky
        else:
            return -1