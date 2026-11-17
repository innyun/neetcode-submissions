class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a, b = 0, 0
        prev = None
        while b < len(nums):
            if prev == nums[b]:
                b += 1
            else:
                prev = nums[b]
                nums[a] = nums[b]
                a += 1
                b += 1

        return a
