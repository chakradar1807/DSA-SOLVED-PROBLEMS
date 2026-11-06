class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        start, end = newInterval

        if n == 0:
            return [newInterval]

        def getIndexBeforeStart():
            if intervals[0][0] >= start:
                return -1

            left, right = 0, n-1
            while left < right:
                mid = (left + right) // 2 + 1
                if intervals[mid][0] < start:
                    left = mid
                else:
                    right = mid -1
            return left

        def getIndexAfterEnd():
            if intervals[n-1][0] <= end:
                return n

            left, right = 0, n-1
            while left < right:
                mid = (left + right) // 2
                if intervals[mid][0] > end:
                    right = mid
                else:
                    left = mid+1
            return left

        i = getIndexBeforeStart()
        j = getIndexAfterEnd()

        if i >= 0 and intervals[i][1] >= start:
            start = intervals[i][0]
            i -= 1
        if j>0:
            end = max(end, intervals[j-1][1])
        result = intervals[:i+1] + [(start, end)] + intervals[j:]
        return result