class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_count=Counter(arr)
        lucky=0
        for i,count in arr_count.items():
            if count>lucky and count==i:
                lucky=count
        if lucky!=0:
            return lucky
        else:
            return -1