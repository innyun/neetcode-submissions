class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []

        for i, n in enumerate(nums): 
            t = -n
            a, b = i + 1, len(nums) - 1
            while a < b:
                if nums[a] + nums[b] == t:
                    r = sorted([nums[a], nums[b], n])
                    if r not in triples:
                        triples.append(r)
                    b -= 1
                    a += 1
                elif nums[a] + nums[b] < t:
                    a += 1
                else:
                    b -= 1

        return triples