class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = None
        k = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
            else:
                prev = nums[i]
                i += 1
                k += 1

        
        return k