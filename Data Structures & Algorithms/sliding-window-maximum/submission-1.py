class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        max_h = []

        for i in range(len(nums)) :
            heapq.heappush(max_h, (-nums[i], i))

            if i >= k - 1: 
                window_start = i - k + 1

                while max_h[0][1] < window_start :
                    heapq.heappop(max_h)
                
                ans.append(-max_h[0][0])

        
        return ans
