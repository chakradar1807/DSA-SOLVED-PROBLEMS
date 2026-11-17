class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    def calculate_score(self, word):
        node = self.root
        score = 0
        for ch in word:
            node = node.children[ch]
            score += node.count
        return score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()

        for word in words:
            trie.insert(word)

        return [trie.calculate_score(word) for word in words]
