class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [n] * n

        dist = n
        for i in range(n):
            if s[i] == c:
                dist = 0
            else:
                dist += 1

            res[i] = dist

        dist = n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                dist = 0
            else:
                dist += 1

            res[i] = min(res[i], dist)

        return res