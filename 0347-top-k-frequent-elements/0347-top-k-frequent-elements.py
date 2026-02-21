class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        # Time: O(n)
        # Space: O(m)  (m = number of unique elements)

        # build max heap
        heap = []
        for num, freq in freqMap.items():
            heapq.heappush(heap, (-freq, num))
        # Time: O(m log m)
        # Space: O(m)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        # Time: O(k log m)

        return result

""" Total time complexity
O(n)          → build frequency map
+ O(m log m)  → build heap
+ O(k log m)  → pop k elements
"""
""" Space Complexity
O(m) → frequency map
O(m) → heap
O(k) → result
So total space O(m)
"""