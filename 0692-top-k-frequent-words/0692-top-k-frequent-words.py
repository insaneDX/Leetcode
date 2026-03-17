class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = Counter()

        for word in words:
            counter[word] += 1
        
        top_k = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:k]
        return [key for key, value in top_k]

        