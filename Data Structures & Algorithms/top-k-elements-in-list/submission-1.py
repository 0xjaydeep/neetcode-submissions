class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []

        for c in count :
            heapq.heappush(h, [count[c],c])
        
        while len(h) != k :
            item = heapq.heappop(h)
            count.pop(item[1])

        return list(count.keys())

