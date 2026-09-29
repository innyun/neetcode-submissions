class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur = []
        visited = [False] * len(nums)

        def backtrack(choices, visited):
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return

            for i, choice in enumerate(choices):
                if visited[i]:
                    continue
                cur.append(choice)
                visited[i] = True
                backtrack(choices, visited)
                cur.remove(choice)
                visited[i] = False

        backtrack(nums, visited)
        return permutations