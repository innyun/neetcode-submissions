class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for s in strs: 
            a[''.join(sorted(s))].append(s)
        
        r = []
        for v in a.values():
            r.append(v)
        return r