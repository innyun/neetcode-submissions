class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for s in strs: 
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            a[tuple(k)].append(s)
        
        return list(a.values())