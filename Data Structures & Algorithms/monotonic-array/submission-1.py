class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = False, False
        n=len(nums)

        if n<2:
            return True
        
        if nums[0]>nums[1]:
            decreasing=True
        else:
            increasing=True
        
        for i in range(1,n):
            if increasing and nums[i-1]>nums[i]:
                return False
            if decreasing and nums[i-1]<nums[i]:
                return False
        
        return True