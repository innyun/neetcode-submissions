class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                j = i + 1
                while j < len(nums):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        k += 1
                        break
                    j += 1
                else:
                    return k
            else:
                k += 1
            i += 1
        return k
            