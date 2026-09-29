class Solution:
    def findMin(self, nums: List[int]) -> int:
        a, b = 0, len(nums) - 1
        ans = nums[0]
        while a <= b:
            if nums[a] <= nums[b]:
                ans = min(nums[a], ans)
                break
            m = (a + b) // 2
            ans = min(nums[m], ans)
            if nums[a] <= nums[m]:
                a = m + 1
            else:
                b = m - 1
        return ans