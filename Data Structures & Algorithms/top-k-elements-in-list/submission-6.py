class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        res=[k for k,v in c.most_common(k)]
        return res