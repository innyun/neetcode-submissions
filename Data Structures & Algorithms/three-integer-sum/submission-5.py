class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []
        l = len(nums)

        for i in range(l): 
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            a, b = i + 1, l - 1

            t = -nums[i]
            while a < b:
                if nums[a] + nums[b] == t:
                    triples.append([nums[i], nums[a], nums[b]])
                
                    while a < b and nums[a + 1] == nums[a]:
                        a += 1
                
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1
                    
                    a += 1
                    b -= 1
                
                elif nums[a] + nums[b] > t:
                    b -= 1
                else:
                    a += 1
        return triples