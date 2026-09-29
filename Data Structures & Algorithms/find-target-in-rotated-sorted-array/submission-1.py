class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        while a <= b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            if nums[b] > nums[m]:
                if target < nums[m] or target > nums[b]:
                    b = m
                else:
                    a = m + 1
            else:
                if target > nums[m] or target < nums[a]:
                    a = m + 1
                else:
                    b = m
        return -1