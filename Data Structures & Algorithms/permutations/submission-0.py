class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        taken=[False]*len(nums)

        def func():
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not taken[i]:
                    curr.append(nums[i])
                    taken[i]=True
                    func()
                    curr.pop()
                    taken[i]=False
        
        func()

        return ans