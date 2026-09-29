class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ft = [0] * 26
            for l in s:
                ft[ord(l) - ord('a')] += 1
            ft = tuple(ft)
            if ft in d.keys():
                d[tuple(ft)].append(s) 
            else:  
                d[tuple(ft)] = [s]
        return list(d.values())