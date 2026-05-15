class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        output = [-1]*len(queries)

        for i in range(len(queries)):
            minSize=float('inf')
            for interval in intervals:
                if interval[0]>queries[i]:
                    break
                if interval[0]<=queries[i]<=interval[1]:
                    minSize=min(minSize, interval[1]-interval[0]+1)
                    output[i]=minSize
        
        return output
