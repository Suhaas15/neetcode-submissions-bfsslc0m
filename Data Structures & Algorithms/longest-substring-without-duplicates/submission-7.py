class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        maxLen = 0
        seen=set()

        while right<len(s):
            if s[right] not in seen:
                seen.add(s[right])
                maxLen = max(maxLen, right-left+1)
                right+=1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
        
        return maxLen
