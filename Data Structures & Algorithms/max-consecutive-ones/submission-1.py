class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=float('-inf')
        for num in nums:
            if num==1:
                count+=1
                max_count = max(count, max_count)
            else:
                count=0
            
        if max_count<0:
            return 0
        else:
            return max_count