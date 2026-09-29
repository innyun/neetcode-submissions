class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        out = []
        for i, n in enumerate(nums):
            target = -n 
            a, b = i + 1, len(nums) - 1
            while a < b:
                if nums[a] + nums[b] > target:
                    b -= 1
                elif nums[a] + nums[b] < target:
                    a += 1
                else:
                    if [n, nums[a], nums[b]] not in out:
                        out.append([n, nums[a], nums[b]])
                    a += 1
                    b -= 1
        return out

                
