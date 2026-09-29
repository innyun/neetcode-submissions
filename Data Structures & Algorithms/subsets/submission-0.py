class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        path = []

        def backtrack(i):
            if i == len(nums):
                sets.append(path.copy())
                return

            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
            backtrack(i + 1)
            
        backtrack(0)

        return sets