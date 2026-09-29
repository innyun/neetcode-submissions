class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
        while i < k:
            heapq.heappush(heap, nums[i])
            i += 1
        while i < len(nums):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
            i += 1
        return heap[0]