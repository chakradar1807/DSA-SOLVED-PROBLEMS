class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        items = [None] * len(freq)
        idx = 0
        for num, f in freq.items():
            items[idx] = (f, num)
            idx += 1
        for i in range(1, len(items)):
            key = items[i]
            j = i - 1
            while j >= 0 and items[j][0] < key[0]:
                items[j + 1] = items[j]
                j -= 1
            items[j + 1] = key
        result = [0] * k
        for i in range(k):
            result[i] = items[i][1]
            
        return result