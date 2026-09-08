class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS, sortedT = sorted(s), sorted(t)

        return sortedS==sortedT