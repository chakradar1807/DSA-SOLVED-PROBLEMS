class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        ds = [[math.sqrt(p[0]*p[0] + p[1]*p[1]),ind]  for ind, p in enumerate(points)]
        
        left = 0
        right = n - 1    

        def partition(left, right):
            pivot = ds[right][0]
            i = left - 1
            for j in range(left, right):
                if pivot >= ds[j][0]:
                    i += 1
                    ds[i], ds[j] = ds[j], ds[i]
            i += 1
            ds[i], ds[right] = ds[right], ds[i]
            return i

        ans = -1

        while left <= right:
            ind = partition(left, right)
            if k == ind+1:
                ans = ind
                break
            if k > ind+1:
                left = ind + 1
            else:
                right = ind - 1


        return [points[ds[i][1]] for i in range(ans+1)]          

            