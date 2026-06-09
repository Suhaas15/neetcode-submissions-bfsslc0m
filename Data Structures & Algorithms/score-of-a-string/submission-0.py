class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        for i in range(1,len(s)):
            total+=abs((ord(s[i])-ord('a')) - (ord(s[i-1])-ord('a')))
        
        return total