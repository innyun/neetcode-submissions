class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        reach = i
        while i > 0:
            found = False
            for j in range(i - 1, -1, -1):
                if nums[j] + j >= i:
                    reach = j
                    found = True
                    break
            if not found:
                return False
            i -= 1

        return True