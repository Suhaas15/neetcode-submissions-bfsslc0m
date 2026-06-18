class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=[]
        for email in emails:
            em=""
            i=0
            while i<len(email):
                if email[i].isalpha():
                    em+=email[i]
                    i+=1
                elif email[i]==".":
                    i+=1
                elif email[i]=="+":
                    while email[i]!="@":
                        i+=1
                    break
                elif email[i]=="@":
                    break
            em+=email[i:]
            if em not in res:
                res.append(em)
        
        return len(res)