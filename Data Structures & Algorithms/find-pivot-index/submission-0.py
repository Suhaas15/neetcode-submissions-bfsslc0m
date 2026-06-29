class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = [0]*len(nums), [0]*len(nums)

        total=nums[0]
        for i in range(1,len(nums)):
            leftSum[i]=total
            total+=nums[i]
        
        total=nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            rightSum[i]=total
            total+=nums[i]
        
        for i in range(len(nums)):
            if leftSum[i]==rightSum[i]:
                return i
        
        return -1