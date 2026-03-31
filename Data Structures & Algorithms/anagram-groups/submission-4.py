class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for string in strs:
            base = sorted(string)
            res[tuple(base)].append(string)
        
        return list(res.values())