class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i, cur, remaining):
            if remaining <= 0 or i == len(candidates):
                cur = sorted(cur)
                if remaining == 0 and cur not in combinations:
                    combinations.append(cur.copy())
                return
            
            cur.append(candidates[i])
            remaining -= candidates[i]
            i += 1
            backtrack(i, cur, remaining)
            t = cur.pop()
            remaining += t
            backtrack(i, cur, remaining)

        backtrack(0, [], target)

        return combinations
