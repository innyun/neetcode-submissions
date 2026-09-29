class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            target = -n 
            a, b = i + 1, len(nums) - 1
            while a < b:
                if nums[a] + nums[b] > target:
                    b -= 1
                elif nums[a] + nums[b] < target:
                    a += 1
                else:
                    out.append([n, nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while nums[a] == nums[a - 1] and a < b:
                        a += 1
        return out
