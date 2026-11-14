class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        
        def match(word: str) -> bool:
            forward = {}
            backward = {}
            for w_char, p_char in zip(word, pattern):
                if w_char in forward and forward[w_char] != p_char:
                    return False
                if p_char in backward and backward[p_char] != w_char:
                    return False
                forward[w_char] = p_char
                backward[p_char] = w_char
            return True

        return [word for word in words if match(word)]