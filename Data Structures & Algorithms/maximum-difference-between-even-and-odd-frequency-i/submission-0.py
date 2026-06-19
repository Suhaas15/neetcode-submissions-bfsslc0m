class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        oddMax, evenMin = 0, len(s)

        for cnt in freq.values():
            if cnt%2==1:
                oddMax = max(oddMax, cnt)
            else:
                evenMin = min(evenMin, cnt)
        
        return oddMax-evenMin