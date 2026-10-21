class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1)
        l2 = len(s2)

        d1 = Counter(s1)
        d2 = Counter(s2[:l1])

        i = 0
        j = l1 - 1

        while j < l2 - 1:
            if d1 == d2:
                return True

            d2[s2[i]] -= 1
            i += 1

            j += 1
            d2[s2[j]] = d2.get(s2[j], 0) + 1

        return d1 == d2