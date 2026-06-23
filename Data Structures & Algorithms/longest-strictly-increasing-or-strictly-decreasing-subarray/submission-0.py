class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        Icount, Dcount=1,1
        maxCount=1

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                Icount+=1
                Dcount=1
            elif nums[i]>nums[i+1]:
                Dcount+=1
                Icount=1
            else:
                Icount=1
                Dcount=1
            
            maxCount = max(maxCount, Icount, Dcount)
        
        return maxCount