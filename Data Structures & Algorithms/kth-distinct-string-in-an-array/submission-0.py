class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}

        for char in arr:
            freq[char] = freq.get(char,0)+1
        
        count=0
        for key, val in freq.items():
            if val==1:
                count+=1
            
            if count==k:
                return key
        
        return ""