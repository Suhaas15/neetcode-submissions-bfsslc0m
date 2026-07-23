class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count=Counter(arr)

        ans=-1
        for key, val in count.items():
            if val==key:
                ans=max(ans, key)
        
        return ans