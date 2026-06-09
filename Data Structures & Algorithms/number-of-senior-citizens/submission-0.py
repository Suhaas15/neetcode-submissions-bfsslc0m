class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for deets in details:
            age = int(deets[-4:-2])
            if age>60:
                count+=1
        
        return count