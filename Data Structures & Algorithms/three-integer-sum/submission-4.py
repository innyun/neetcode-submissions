class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []

        for i, n in enumerate(nums): 
            if i > 0 and n == nums[i - 1]:
                continue
            t = -n
            a, b = i + 1, len(nums) - 1
            while a < b:
                if nums[a] + nums[b] == t:
                    r = [n, nums[a], nums[b]]
                    triples.append(r)
                    while a < b and nums[a] == nums[a + 1]:
                        a += 1
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1
                    a += 1
                    b -= 1
                elif nums[a] + nums[b] < t:
                    a += 1
                else:
                    b -= 1

        return triples