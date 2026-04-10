class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter


        count = Counter(nums)
        topK = []
        for word, freq in count.most_common(k):
            topK.append(word)
        return topK
