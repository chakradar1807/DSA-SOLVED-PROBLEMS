class Solution:
    def repeatedStringMatch(self, a, b):
        repeat = (len(b)//len(a))
        count = 1
        while count <= repeat + 2:
            if b in a*count:
                return count
            else:
                count += 1
        return -1