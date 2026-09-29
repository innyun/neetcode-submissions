class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur = []

        def backtrack(choices):
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return

            for choice in choices:
                cur.append(choice)
                t = choices.copy()
                t.remove(choice)
                backtrack(t)
                cur.remove(choice)

        backtrack(nums)
        return permutations