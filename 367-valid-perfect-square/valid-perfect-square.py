class Solution:
    def isPerfectSquare(self,x):
        if x==1:
            return True
        left,right=2,x//2
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return True
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return False