class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""

        for ch in s:
            if ch.isalnum():
                tmp += ch

        tmp = tmp.lower()

        i = 0
        j = len(tmp) - 1

        while i < j:
            if tmp[i] != tmp[j]:
                return False

            i += 1
            j -= 1

        return True