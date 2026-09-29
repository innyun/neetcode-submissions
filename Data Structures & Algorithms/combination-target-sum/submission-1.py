class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        cur = []
        s = 0

        def backtrack(i):
            nonlocal s
            if s >= target:
                if s == target:
                    combinations.append(cur.copy())
                return
        
            for j in range(i, len(nums)):
                n = nums[j]
                cur.append(n)
                s += n
                backtrack(j)
                cur.pop()
                s -= n
            
        backtrack(0)

        return combinations