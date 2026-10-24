

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()                     
        cur = head
        while cur:
            nxt = cur.next                       
         
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            cur.next = prev.next                
            prev.next = cur
            cur = nxt                            
        return dummy.next