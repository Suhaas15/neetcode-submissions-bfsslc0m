class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]

        for startA, endA in firstList:
            for startB, endB in secondList:
                if (startA <= startB <= endA) or (startB <= startA <= endB):
                    res.append([max(startA, startB), min(endA, endB)])
        
        return res