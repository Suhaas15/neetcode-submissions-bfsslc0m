# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return 
        
        #count total nodes
        curr=head 
        count=0 
        while curr: 
            count+=1 
            curr=curr.next 
        
        #no of times needed to reverse 
        rTimes = count//k 
        
        #reverse in batches 
        curr=head
        newHead=None
        tail=None
        for _ in range(rTimes): 
            groupPrev=None
            groupHead=curr 
            for _ in range(k): 
                temp=curr.next 
                curr.next=groupPrev 
                groupPrev=curr 
                curr=temp
            
            if not newHead:
                newHead=groupPrev
            if tail:
                tail.next=groupPrev
            tail=groupHead
        if tail:
            tail.next = curr
        return newHead if newHead else None




