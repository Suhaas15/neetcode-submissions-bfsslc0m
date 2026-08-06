class Solution:
    def minOperations(self, s: str) -> int:
        check=int(s[0])
        count=0

        for i in range(1, len(s)):
            if i%2!=0:
                if int(s[i])==check:
                    count+=1
            else:
                if int(s[i])!=check:
                    count+=1
        
        return min(count, len(s)-count)