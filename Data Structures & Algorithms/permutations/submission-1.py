class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur = []

        def backtrack(choices, visited):
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return

            for choice in choices:
                if choice in visited:
                    continue
                cur.append(choice)
                visited.add(choice)
                backtrack(choices, visited)
                cur.remove(choice)
                visited.remove(choice)

        backtrack(nums, set())
        return permutations