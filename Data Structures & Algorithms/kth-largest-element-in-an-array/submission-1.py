class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums: 
            if k == 0: 
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)
                k -= 1
        
        return h[0]
